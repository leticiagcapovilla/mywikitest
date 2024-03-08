---
title: Trackcpp
description: 
published: 1
date: 2024-03-05T14:57:06.448Z
tags: 
editor: markdown
dateCreated: 2024-03-05T14:53:32.984Z
---

# FAC: Trackcpp

Tracking code library written in C++ to calculate beam optics and dynamical apertures. It is supposed to be used as a library to be linked with other C++ codes, as a python module to be imported or a script-driven command-line tool that reads input files and writes output data. The code is at [GitHub trackcpp repository](https://github.com/lnls-fac/trackcpp)

## As a C++ library

The library defines a simple structure called `Accelerator` in `trackcpp/accelerator.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/accelerator.h)) whose objects specify beam, lattice, simulation flags and auxilliary data structures (IDs kicktables, for example): 

```
struct Accelerator {
        double                  energy;           // [eV] 
        bool                    cavity_on;
        bool                    radiation_on;
        bool                    vchamber_on;
        int                     harmonic_number;
        std::vector<Element>    lattice;
        std::vector<Kicktable*> kicktables;
};

```

The lattice is defined, as in most other tracking codes, as a list of elements. Class `Element` in `trackcpp/elements.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/elements.h)) contains a list of static syntactic sugar methods to help creating particular types of lattice elements: 

```
// front-end routines for typed element creation
static Element marker     (const std::string& fam_name_);
static Element bpm        (const std::string& fam_name_);
static Element hcorrector (const std::string& fam_name_, const double& length_, const double& hkick_);
static Element vcorrector (const std::string& fam_name_, const double& length_, const double& vkick_);
static Element corrector  (const std::string& fam_name_, const double& length_, const double& hkick_, const double& vkick_);
static Element drift      (const std::string& fam_name_, const double& length_);
static Element rbend      (const std::string& fam_name_, const double& length_, const double& angle_, 
                           const double& angle_in_ = 0, const double& angle_out_ = 0, const double& K_ = 0, const double& S_ = 0);
static Element quadrupole (const std::string& fam_name_, const double& length_, const double& K_, const int nt_steps_ = 1);
static Element sextupole  (const std::string& fam_name_, const double& length_, const double& S_, const int nr_steps_ = 1);
static Element rfcavity   (const std::string& fam_name_, const double& length_, const double& frequency_, const double& voltage_);
```

The solutions of the particle equations of motion are implemented as template passmethods in `trackcpp/passmethods.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/passmethods.h)). Each passmethod may be invoked with floating point 6D electron phase space coordinates (numerical tracking) or with TPSA coordinates (differencial algebra tracking). In other words, arbitrary-order non-linear maps (transfer maps or one-turn maps) with machine precision can be extracted. One advantage of having DA tracking is to be able to obtain opticas parameters of any order (chromaticities, compaction factors, etc) without resorting to numerical derivatives which are can be plagged with numerical imprecisionor to error-prone human-derived higher order perturbation expressions. The differential algebra is implemented in `trackcpp/tpsa.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/tpsa.h)).

For example, a simple FODO lattice with a 3 GeV beam is created as in 

```
double ds_length =  1.0; // [m]
double qf_length =  0.1; // [m]
double qd_length =  0.1; // [m]
double qf_K      =  0.5; // [1/m^2]
double qd_K      = -0.5; // [1/m^2]
```

```
qf = Element::quadrupole("QF", qf_length, qf_K);
qd = Element::quadrupole("QD", qd_length, qd_K);
ds = Element::drift("DS", ds_length);
```

```
Accelerator the_ring;
the_ring.energy = 3.0e9; // [eV]
the_ring.lattice = {qf, ds, qd, ds};
```

The function `sirius_v500` in `trackcpp/sirius_v500.cpp` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/sirius_v500.cpp)) builds the Sirius lattice version V500 mode AC10. A lattice can also be imported from an ASCII tracy-like flat file using the function `read_flat_file_tracy` defined in `trackcpp/flat_file_tracy.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/flat_file_tracy.h)). Functions in `trackcpp/kicktable.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/kicktable.h)) can be used to create programmatically a RADIA kicktable and insert it in the lattice or to read it from a file. There are a number of functions defined in `trackcpp/lattice.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/lattice.h)) for manipulating lattices: 

```
std::vector<Element> latt_join(const std::vector<std::vector<Element> >& v_);
std::vector<Element> latt_reverse(const std::vector<Element>& v_);
void                 latt_print(const std::vector<Element>& lattice);
std::vector<int>     latt_range(const std::vector<Element>& lattice);
std::vector<double>  latt_findspos(const std::vector<Element>& lattice, const std::vector<int>& idx);
double               latt_findspos(const std::vector<Element>& lattice, const int idx);
void                 latt_setcavity(std::vector<Element>& lattice, const std::string& state);
std::vector<Element> latt_set_num_integ_steps(const std::vector<Element>& orig_lattice);
std::vector<Element> latt_read_flat_file(const std::string& filename);
Status::type         latt_read_flat_file(const std::string& filename, Accelerator& accelerator);
std::vector<int>     latt_findcells_fam_name    (const std::vector<Element>& lattice, const std::string& value, bool reverse = false);
std::vector<int>     latt_findcells_angle       (const std::vector<Element>& lattice, const double& value,      bool reverse = false);
std::vector<int>     latt_findcells_frequency   (const std::vector<Element>& lattice, const double& value,      bool reverse = false);
std::vector<int>     latt_findcells_polynom_b   (const std::vector<Element>& lattice, unsigned int n, const double& value, bool reverse = false);
std::vector<int>     latt_findcells_polynom_a   (const std::vector<Element>& lattice, unsigned int n, const double& value, bool reverse = false);
std::vector<int>     latt_findcells_pass_method (const std::vector<Element>& lattice, const std::string& value, bool reverse = false);
```

Once the lattice, beam parameters and simulation flags are defined, tracking or beam dynamics optics properties can be calculated. Tracking functions are defined in `/trackc++/tracking.h` ([Github file](https://github.com/lnls-fac/fac_code/trackcpp/blob/master/tracking.h)): 

```
template <typename T> Status::type track_elementpass (
                                   const Element& el,              // element through which to track particle
                                   Pos<T> &orig_pos,               // initial electron coordinates
                                   const Accelerator& accelerator);
template <typename T> Status::type track_linepass (
                                   const Accelerator& accelerator, 
                                   Pos<T>& orig_pos,               // initial electron coordinates
                                   std::vector<Pos<T> >& pos,      // vector with electron coordinates from tracking at every element
                                   unsigned int& element_offset,   // index of starting element for tracking
                                   Plane::type& lost_plane,        // return plane in which particle was lost, if the case
                                   bool trajectory)                // whether function should return coordinates at all elements
template <typename T> Status::type track_ringpass (
                                   const Accelerator& accelerator,
                                   Pos<T> &orig_pos,               // initial electron coordinates
                                   std::vector<Pos<T> > &pos,      // vector with electron coordinates from tracking at every element, every turn.
                                   const unsigned int nr_turns,    // number of turns to track
                                   unsigned int &lost_turn,        // returns turn where particle was lost, if the case	                    
                                   unsigned int &element_offset,   // index of starting element for tracking
                                   Plane::type& lost_plane,        // return plane in which particle was lost, if the case
                                   bool trajectory)                // whether function should return coordinates at all elements, all turns
```

```
Status::type track_findorbit6 (  // returns the 6D closed orbit around the ring
             const Accelerator& accelerator, 
             std::vector<Pos<double> >& close_orbit);
Status::type track_findm66 (     // uses DA tracking to extract exact (machine precision) one-turn matrices for Twiss parameters calculations
             const Accelerator& accelerator, 
             const std::vector<Pos<double> >& closed_orbit, 
             std::vector<double*> m66);
```

Functions that calculates optics parameters such as tunes, beta functions, chromaticities are defined in `trackcpp/optics.h` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/optics.h)). Dynamical aperture calculations are all defined in `trackcpp/dynap.cpp` ([Github file](https://github.com/lnls-fac/trackcpp/blob/master/dynap.cpp)): 

```
Status::type dynap_xy(   // calculates dynamical aperture in the xy plane
             const Accelerator& accelerator,
             std::vector<Pos<double> >& cod,
             unsigned int nr_turns,
             const Pos<double>& p0,
             unsigned int nrpts_x, double x_min, double x_max,
             unsigned int nrpts_y, double y_min, double y_max,
             bool calculate_closed_orbit,
             std::vector<DynApGridPoint>& grid,
             unsigned int nr_threads);
Status::type dynap_ex(   // calculates dynamical aperture in the ex plane
             const Accelerator& accelerator,
             std::vector<Pos<double> >& cod,
             unsigned int nr_turns,
             const Pos<double>& p0,
             unsigned int nrpts_e, double e_min, double e_max,
             unsigned int nrpts_x, double x_min, double x_max,
             bool calculate_closed_orbit,
             std::vector<DynApGridPoint>& grid,
             unsigned int nr_threads);
Status::type dynap_ma(   // calculates momentum acceptance along the ring
             const Accelerator& accelerator,
             std::vector<Pos<double> >& cod,
             unsigned int nr_turns,
             const Pos<double>& p0,
             const double& e0,
             const double& e_tol,
             const double& s_min, const double& s_max,
             const std::vector<std::string>& fam_names,
             bool calculate_closed_orbit,
             std::vector<DynApGridPoint>& grid,
             unsigned int nr_threads);
Status::type dynap_xyfmap(   // calculates frequency map in the xy plane
             const Accelerator& accelerator,
             std::vector<Pos<double> >& cod,
             unsigned int nr_turns,
             const Pos<double>& p0,
             unsigned int nrpts_x, double x_min, double x_max,
             unsigned int nrpts_y, double y_min, double y_max,
             bool calculate_closed_orbit,
             std::vector<DynApGridPoint>& grid,
             unsigned int nr_threads);
Status::type dynap_exfmap(   // calculates frequency map in the ex plane
             const Accelerator& accelerator,
             std::vector<Pos<double> >& cod,
             unsigned int nr_turns,
             const Pos<double>& p0,
             unsigned int nrpts_e, double e_min, double e_max,
             unsigned int nrpts_x, double x_min, double x_max,
             bool calculate_closed_orbit,
             std::vector<DynApGridPoint>& grid,
             unsigned int nr_threads);
```

Finally the file `trackc++/commands.h` ([Github file](https://github.com/lnls-fac/trackcblob/master/commands.h)) defines all functionalities that can be invoked through the Linux command-line. 

## As a script-driven tool

Trackcpp can be invoked from within a script, be it in Python or in Bash. For example, from the bash prompt a call to the executable `trackcpp` without arguments should print info on the running version of the code: 

```
ximenes@lnls208-linux:~$ trackcpp
# TRACKCPP version(Jul 10 2014 16:30:51)
# Accelerator Physics Group - LNLS
# Campinas BRAZIL
# contact: xresende@gmail.com
```

It is assumed that the executable `trackcpp` is in the bash path. Usually there should be a symbolic link in `~/bin` to it. The first argument tells which command is to be run by `trackcpp`. These are the commands which are defined and corresponding arguments: 

```
(arg01) dynap_xy          calculation of dynamical aperture projected on xy plane.
(arg02) flat_filename     flat filename with lattice to be loaded
(arg03) ring_energy       [eV]
(arg04) harmonic_number   
(arg05) cavity_state      "on" or "off"
(arg06) radiation_state   "on" or "off"
(arg07) vchamber_state    "on" or "off"
(arg08) de0               fixed de0 to launch particles with for tracking
(arg09) nr_turns          number of turns to track
(arg10) x_nrpts           number of points in horizontal grid
(arg11) x_min             minimum horizontal coordinate value [m] 
(arg12) x_max             maximum horizontal coordinate value [m] 
(arg13) y_nrpts           number of points in vertical grid
(arg14) y_min             minimum vertical coordinate value [m] 
(arg15) y_max             maximum vertical coordinate value [m]
(arg16) nr_threads        number of threads to use (optional)
```

```
(arg01) dynap_ex          calculation of dynamical aperture projected on ex plane.
(arg02) flat_filename     flat filename with lattice to be loaded
(arg03) ring_energy       [eV]
(arg04) harmonic_number   
(arg05) cavity_state      "on" or "off"
(arg06) radiation_state   "on" or "off"
(arg07) vchamber_state    "on" or "off"
(arg08) y0                fixed y to launch particles with for tracking
(arg09) nr_turns          number of turns to track
(arg10) e_nrpts           number of points in energy grid
(arg11) e_min             minimum energy coordinate value 
(arg12) e_max             maximum energy coordinate value 
(arg13) x_nrpts           number of points in horizontal grid
(arg14) x_min             minimum horizontal coordinate value [m] 
(arg15) x_max             maximum horizontal coordinate value [m]
(arg16) nr_threads        number of threads to use (optional)
```

```
(arg01) dynap_ma          calculation of momentum acceptance around ring.
(arg02) flat_filename     flat filename with lattice to be loaded
(arg03) ring_energy       [eV]
(arg04) harmonic_number   
(arg05) cavity_state      "on" or "off"
(arg06) radiation_state   "on" or "off"
(arg07) vchamber_state    "on" or "off"
(arg08) nr_turns          number of turns to track
(arg09) y0                fixed y to launch particles with for tracking
(arg10) e0                
(arg11) e_tol
(arg12) s_min
(arg13) s_max                
(arg14) nr_threads        number of threads to use (optional)
(arg15) fam_names

(arg01) dynap_xyfmap      calculation of frequency map on xy plane.
(arg02) flat_filename     flat filename with lattice to be loaded
(arg03) ring_energy       [eV]
(arg04) harmonic_number   
(arg05) cavity_state      "on" or "off"
(arg06) radiation_state   "on" or "off"
(arg07) vchamber_state    "on" or "off"
(arg08) de0               fixed de0 to launch particles with for tracking
(arg09) nr_turns          number of turns to track
(arg10) x_nrpts           number of points in horizontal grid
(arg11) x_min             minimum horizontal coordinate value [m] 
(arg12) x_max             maximum horizontal coordinate value [m] 
(arg13) y_nrpts           number of points in vertical grid
(arg14) y_min             minimum vertical coordinate value [m] 
(arg15) y_max             maximum vertical coordinate value [m]
(arg16) nr_threads        number of threads to use (optional)
```

```
(arg01) dynap_exfmap      calculation of frequency map on ex plane.
(arg02) flat_filename     flat filename with lattice to be loaded
(arg03) ring_energy       [eV]
(arg04) harmonic_number   
(arg05) cavity_state      "on" or "off"
(arg06) radiation_state   "on" or "off"
(arg07) vchamber_state    "on" or "off"
(arg08) y0                fixed y to launch particles with for tracking
(arg09) nr_turns          number of turns to track
(arg10) e_nrpts           number of points in energy grid
(arg11) e_min             minimum energy coordinate value 
(arg12) e_max             maximum energy coordinate value 
(arg13) x_nrpts           number of points in horizontal grid
(arg14) x_min             minimum horizontal coordinate value [m] 
(arg15) x_max             maximum horizontal coordinate value [m]
(arg16) nr_threads        number of threads to use (optional)
```

```
(arg01) track_linepass    one particle, one turn tracking from initial coordinates.
(arg02) flat_filename     flat filename with lattice to be loaded
(arg03) ring_energy       [eV]
(arg04) harmonic_number   
(arg05) cavity_state      "on" or "off"
(arg06) radiation_state   "on" or "off"
(arg07) vchamber_state    "on" or "off"
(arg08) rx0               initial x coordinate [m]
(arg09) px0               initial x' coordinate
(arg10) ry0               initial y coordinate [m]
(arg11) py0               initial y' coordinate
(arg12) de0               initial energy offset coordinate
(arg13) dl0               initial longitudinal offset coordinate [m]
```

 For example, the command 
 
 `ximenes@lnls208-linux:~$ trackcpp dynap_xy "/home/fac_files/code/python/trackcpp/pytrack/sirius_v500_ac10_5_bare_in.txt" \ 
3.0e9 864 on on on 0.01 5000 30 -0.010 0.010 20 0.0 0.005 4`

will calculate the xy dynamical aperture within the regular grid of 30 horizontal points from -10 mm to +10 mm, 20 vertical points from 0 mm to 5 mm, for 5000 turns and energy offset of 1%. It will use 4 parallel threads. 

## PyAccel

see [FAC: Pyaccel][link]

## Todo list

* check algorithm for energy acceptance calculations along the ring.
* advertise python scripts that drive trackcpp.