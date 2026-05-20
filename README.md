# ROS2 Docker Codespaces Starter

A lightweight ROS2 Humble development environment using Docker, DevContainers and GitHub Codespaces.

## Objective

This project provides a reproducible ROS2 development environment without requiring a local Linux or Docker installation.

It is designed for learning and prototyping ROS2 applications in the cloud.

## Tech Stack

- ROS2 Humble
- Ubuntu 22.04
- Docker
- GitHub Codespaces
- VS Code DevContainers
- Python
- colcon

## Project Structure

```text
.
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── ros2_ws/
│   └── src/
│       └── robot_status_demo/
└── README.md