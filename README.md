# CompareCompilers - Suite of Computational Kernels to test C/C++ compilers
Computations for checking performance of different compilers.\
This code Contains 3 different computational kernels for performance assesment of processors using code compiled with Intel and AMD compilers.\
Kernal 1. A straightforward implementation of the pivotless LU decomposition with simple data structures and memory access pattern, and without any hand-tuning. Although this kernel can be optimized to the point at which it is compute bound, we test the un-optimized version of the kernel in order to determine how each compiler handles ‘naive’ source code with complex vectorization and threading patterns hidden within.\
Kernal 2. A highly abstracted object-oriented implementation of a Jacobi solver for the Poisson problem on a square domain. This kernel tests how well the compilers can perform complex, cross-procedural code analysis to detect common parallel patterns (in this case, a 5-point stencil). This is a bandwidth-bound kernel, meaning that its performance is limited by the RAM bandwidth rather than by the floating-point arithmetic capabilities of the cores.\
Kernel 3. A heavily-tuned implementation of structure function computation. We fully optimize this kernel to the point where it is compute-bound, i.e., limited by the arithmetic performance capabilities of the CPU. The purpose of this test is to see how efficient the resulting binary is when the source code is acutely aware of the underlying architecture.
# How to Build and Run
clone the repository\
For on-prem HPC just execute the build.bash script from a build directory, one level up the cloned directory.\
you can pass 3 types of params to the build.bash script;\
-u <amd/intel> -> the choice of the c/c++ compiler vendors.\
-a <llvm> -> must be used wuth intel option to choose the Intel LLVM compiler.\
-f <yes> -> to run the application JacobiSolve.\
For Windows, use cmake-gui to configure and build a VS solution and then run is as usual. Make sure you have the intel-MPI installed on your system. Try between MSVC
intel compilers on Windows.
