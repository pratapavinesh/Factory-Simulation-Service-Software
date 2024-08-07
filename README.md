# <div align="center">Factory Simulation Service Software</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/pratapavinesh/Factory-Simulation-Service-Software/main/images/demo.png" alt="Demo" width="600"/>
</div>

## Overview

This software simulates factory operations, allowing the head/owner and manager to manage and analyze factory efficiency over long periods. The simulation provides insights into machine utilization, adjuster utilization, and overall factory performance.

## Features

### Head/Owner Role

- **View All Machines and Works**: After signing in, the head/owner can view the status of all machines and the ongoing work.
- **Simulate Factory Operations**: The head/owner can simulate the factory operations for up to 100 years to analyze the results, such as:
  - Average Machine Utilization
  - Average Adjuster Utilization
  - Utilization of each machine
  - Utilization of each adjuster

<div align="center">
  <img src="https://raw.githubusercontent.com/pratapavinesh/Factory-Simulation-Service-Software/main/images/head.png" alt="Head Dashboard" width="600"/>
</div>

#### Example Output
```json
{
  "avg_machine_util": 92.27,
  "avg_adjuster_util": 14.44,
  "machine_util": {
    "1": 92.27,
    "2": 92.27
  },
  "adjuster_util": {
    "1": 14.44
  }
}
```

### Manager Role

- **Add New Machines**: The manager can add new machines to the factory.
- **Assign Work to Workers**: The software automatically assigns work to available workers who have the required skills.

<div align="center">
  <img src="https://raw.githubusercontent.com/pratapavinesh/Factory-Simulation-Service-Software/main/images/manager.png" alt="Manager Dashboard" width="600"/>
</div>

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries: `flask`, `pandas`, `numpy`, etc.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/pratapavinesh/factory-simulation-service-software.git
    cd factory-simulation-service-software
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Software

1. Start the Flask server:
    ```sh
    python main.py
    ```

2. The login window will open.

## Usage

### Head/Owner Role

1. **Sign In**: Use your credentials to sign in as the head/owner.
2. **View Machines and Works**: Navigate to the dashboard to view all machines and ongoing works.
3. **Simulate Operations**: Use the simulation feature to analyze factory performance for up to 100 years.

### Manager Role

1. **Sign In**: Use your credentials to sign in as the manager.
2. **Add New Machines**: Navigate to the 'Add Machines' section to register new machines in the factory.

## License

Distributed under the MIT License. See `LICENSE` for more information.
