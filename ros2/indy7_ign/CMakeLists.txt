cmake_minimum_required(VERSION 3.5)
project(indy7_ign)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

# Install directories
install(DIRECTORY urdf indy7/meshes launch rviz DESTINATION share/${PROJECT_NAME})

# Setup the project
ament_package()