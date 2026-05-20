FROM ros:humble-ros-base-jammy

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

# Basic tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    nano \
    vim \
    tree \
    build-essential \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep safely
RUN if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then \
        rosdep init; \
    fi && rosdep update

# Create workspace
WORKDIR /workspaces/ros2-docker-codespaces-starter

# Source ROS2 automatically
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
RUN echo "if [ -f /workspaces/ros2-docker-codespaces-starter/ros2_ws/install/setup.bash ]; then source /workspaces/ros2-docker-codespaces-starter/ros2_ws/install/setup.bash; fi" >> /root/.bashrc

CMD ["/bin/bash"]