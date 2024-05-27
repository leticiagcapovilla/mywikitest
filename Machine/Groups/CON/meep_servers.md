# CON: Meep servers

## Introduction

[Meep](https://meep.readthedocs.io/en/latest/){target=_blank} is a free and open-source software package for simulating electromagnetic systems via the finite-difference time-domain (FDTD) method. This document page details the steps needed to set the system up in our [CON:Sirius_control_system_servers|servers](link) and is based on this [tutorial](http://geek-mag.com/posts/248514/){target=_blank}.

## Installation

First, install needed compilers and dependences which are available in the CentOS' official repositories:

```
$ sudo yum install libtool* mpich-devel.* lapack* guile guile-devel readline-devel gcc-c++ scalapack-* paraview*
```

Next, edit the user's `.bashrc` adding the following environment variables. Those variables refer to the directories where the MEEP libraries and binaries will be installed.

```
$ nano /home/<user>/.bashrc

export LDFLAGS="-L/usr/local/lib -lm"
export CPPFLAGS="-I/usr/local/include"
export LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
export PATH="/lib64/mpich/bin:$PATH"
```

### HDF5

The next step is to install the HDF5 packages with [parallel support](https://support.hdfgroup.org/ftp/HDF5/current/src/unpacked/release_docs/INSTALL_parallel){target=_blank} under `/usr/local`. First, download the packages into the `Software` folder:

```
$ mkdir Software
$ cd Software
$ wget https://support.hdfgroup.org/ftp/HDF5/current18/src/hdf5-1.8.20.tar.gz
$ tar -xf hdf5-1.8.20.tar.gz
```

Compile the packages and install it:

```
$ cd hdf5-1.8.20/
$ CC=/lib64/mpich/bin/mpicc ./configure --enable-parallel --prefix=/usr/local
$ make -j16
$ make check
$ sudo make install
```

### FFTW

To install FFTW library with MPI support, execute the following steps inside `Software/`:

```
$ wget http://www.fftw.org/fftw-3.3.8.tar.gz
$ tar -xf fftw-3.3.8.tar.gz
$ cd fftw-3.3.8/
$ CC=/lib64/mpich/bin/mpicc CXX=/lib64/mpich/bin/mpicxx F77=/lib64/mpich/bin/mpif77 ./configure --enable-mpi --enable-openmp
$ make -j16
$ sudo make install
```

### Libctl

Compile Libctl source files:

```
$ wget https://github.com/stevengj/libctl/releases/download/v4.1.0/libctl-4.1.0.tar.gz
$ tar -xf libctl-4.1.0.tar.gz
$ cd libctl-4.1.0/
$ CC=/lib64/mpich/bin/mpicc CXX=/lib64/mpich/bin/mpicxx F77=/lib64/mpich/bin/mpif77 ./configure
$ make -j16
$ sudo make install
```

### MPB

Compile MPB source files with MPI and OpenMP support:

```
$ wget https://github.com/stevengj/mpb/releases/download/v1.6.2/mpb-1.6.2.tar.gz
$ tar -xf mpb-1.6.2.tar.gz
$ cd mpb-1.6.2/
$ CC=/lib64/mpich/bin/mpicc CXX=/lib64/mpich/bin/mpicxx F77=/lib64/mpich/bin/mpif77 ./configure --with-mpi --with-openmp
$ make -j16
$ sudo make install
```

### Harminv

Similarly, we compile the files directly from the Github project:

```
$ wget https://github.com/stevengj/harminv/releases/download/v1.4.1/harminv-1.4.1.tar.gz
$ tar -xf harminv-1.4.1.tar.gz
$ cd harminv-1.4.1/
$ CC=/lib64/mpich/bin/mpicc CXX=/lib64/mpich/bin/mpicxx F77=/lib64/mpich/bin/mpif77 ./configure
$ make
$ sudo make install
```

### MEEP

Finally, we install MEEP with MPI, OpenMP and Python3 support:

```
$ wget https://github.com/stevengj/meep/releases/download/v1.5.0/meep-1.5.tar.gz
$ tar -xf meep-1.5.tar.gz
$ cd meep-1.5/
$ PYTHON=python3 CC=/lib64/mpich/bin/mpicc CXX=/lib64/mpich/bin/mpicxx C++=/lib64/mpich/bin/mpic++ F77=/lib64/mpich/bin/mpif77 ./configure --with-mpi
$ make
$ sudo make install
```

Test it with

```
$ make check
```

### h5utils

The last step is to install h5utils package:

```
$ wget https://github.com/stevengj/h5utils/releases/download/1.13.1/h5utils-1.13.1.tar.gz
$ tar -xf h5utils-1.13.1.tar.gz
$ cd h5utils-1.13.1/
$ CC=/lib64/mpich/bin/mpicc CXX=/lib64/mpich/bin/mpicxx F77=/lib64/mpich/bin/mpif77 ./configure
$ make -j4 
$ sudo make install
```
