cmake_minimum_required(VERSION 3.5)
project(indy7_moveit2_config)

# Find dependencies
find_package(ament_cmake REQUIRED)

# Install directories
install(DIRECTORY config srdf launch DESTINATION share/${PROJECT_NAME})

# Setup the project
ament_package()
