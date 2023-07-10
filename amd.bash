#! /bin/bash

[[ -r /glb/apps/hpc/EasyBuild/Public/Lmod/etc/profile.d/z01_lmod-hpcti.sh ]] && . /glb/apps/hpc/EasyBuild/Public/Lmod/etc/profile.d/z01_lmod-hpcti.sh -n

module load CMake/3.23.1-GCCcore-11.3.0


while getopts u:a:f: flag
do
    case "${flag}" in
        u) comptype=${OPTARG};;
        a) age=${OPTARG};;
        f) fullname=${OPTARG};;
    esac
done
echo "Username: $username";
echo "Age: $age";
echo "Full Name: $fullname";

if [ ${comptype}=="amd" ];then
	module swap HpctiSoftwareStack/PRODUCTION HpctiSoftwareStack/ACCEPTANCE
	module load AOCC/4.0.0-GCCcore-11.3.0
	CC=clang CXX=clang++ cmake -DCMAKE_BUILD_TYPE=Release ../CompareCompilers/
fi


cmake --build .