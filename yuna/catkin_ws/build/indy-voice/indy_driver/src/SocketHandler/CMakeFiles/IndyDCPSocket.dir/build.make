# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/choi/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/choi/catkin_ws/build

# Include any dependencies generated for this target.
include indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/depend.make

# Include the progress variables for this target.
include indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/progress.make

# Include the compile flags for this target's objects.
include indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/flags.make

indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.o: indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/flags.make
indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.o: /home/choi/catkin_ws/src/indy-voice/indy_driver/src/SocketHandler/IndyDCPSocket.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/choi/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.o"
	cd /home/choi/catkin_ws/build/indy-voice/indy_driver/src/SocketHandler && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.o -c /home/choi/catkin_ws/src/indy-voice/indy_driver/src/SocketHandler/IndyDCPSocket.cpp

indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.i"
	cd /home/choi/catkin_ws/build/indy-voice/indy_driver/src/SocketHandler && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/choi/catkin_ws/src/indy-voice/indy_driver/src/SocketHandler/IndyDCPSocket.cpp > CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.i

indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.s"
	cd /home/choi/catkin_ws/build/indy-voice/indy_driver/src/SocketHandler && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/choi/catkin_ws/src/indy-voice/indy_driver/src/SocketHandler/IndyDCPSocket.cpp -o CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.s

# Object files for target IndyDCPSocket
IndyDCPSocket_OBJECTS = \
"CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.o"

# External object files for target IndyDCPSocket
IndyDCPSocket_EXTERNAL_OBJECTS =

/home/choi/catkin_ws/devel/lib/libIndyDCPSocket.so: indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/IndyDCPSocket.cpp.o
/home/choi/catkin_ws/devel/lib/libIndyDCPSocket.so: indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/build.make
/home/choi/catkin_ws/devel/lib/libIndyDCPSocket.so: indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/choi/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library /home/choi/catkin_ws/devel/lib/libIndyDCPSocket.so"
	cd /home/choi/catkin_ws/build/indy-voice/indy_driver/src/SocketHandler && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/IndyDCPSocket.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/build: /home/choi/catkin_ws/devel/lib/libIndyDCPSocket.so

.PHONY : indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/build

indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/clean:
	cd /home/choi/catkin_ws/build/indy-voice/indy_driver/src/SocketHandler && $(CMAKE_COMMAND) -P CMakeFiles/IndyDCPSocket.dir/cmake_clean.cmake
.PHONY : indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/clean

indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/depend:
	cd /home/choi/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/choi/catkin_ws/src /home/choi/catkin_ws/src/indy-voice/indy_driver/src/SocketHandler /home/choi/catkin_ws/build /home/choi/catkin_ws/build/indy-voice/indy_driver/src/SocketHandler /home/choi/catkin_ws/build/indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : indy-voice/indy_driver/src/SocketHandler/CMakeFiles/IndyDCPSocket.dir/depend
