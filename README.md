### Ransomware Spread Simulation Environment

#### Introduction
This project simulates the spread of ransomware across a peer-to-peer network to evaluate the effectiveness of different mitigation strategies. The simulation uses a graph to represent a network, where nodes represent devices and edges represent connections between them. The ransomware spreads through this network, allowing the user to apply different strategies to mitigate the spread.

#### Features
- **Network Representation**: A peer-to-peer network of nodes is generated using NetworkX.
- **Ransomware Spread**: Simulates the spread of ransomware based on infection probability.
- **Mitigation Strategies**: Different strategies are implemented to mitigate ransomware:
  - **Isolation**: Disconnect infected nodes from their neighbors.
  - **Patch**: Patch healthy nodes to make them immune to infection.
  - **Backup**: Restore infected nodes to their healthy state from backup.
- **Visualization**: Provides visual representations of the network's state at each stage of the simulation.

#### Usage Instructions
1. **Setup Dependencies**: Install necessary Python packages using `pip`.
    ```sh
    pip install networkx matplotlib
    ```
2. **Run the Simulation**: Use the following command to start the simulation.
    ```sh
    python ransomware_spread_simulation.py
    ```

#### How It Works
1. **Network Creation**: A graph-based representation of a peer-to-peer network is created, where nodes are assigned as either healthy or infected based on an initial probability.
2. **Ransomware Spread**: In each round, infected nodes attempt to infect their neighbors with a given probability.
3. **Mitigation Strategies**: Every few rounds, a mitigation strategy is applied to evaluate its effectiveness against ransomware spread.
4. **Logging and Visualization**: The spread of ransomware and the application of mitigation strategies are logged, and the network state is visualized at each step.

#### Mitigation Strategies
- **Isolation**: Disconnects infected nodes from the rest of the network, preventing further spread.
- **Patch**: Protects healthy nodes by patching them, making them immune to infection.
- **Backup**: Attempts to restore infected nodes to their original healthy state.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Use the command `pip install -r requirements.txt` to install dependencies.
3. **Run the Tool**: Execute `python ransomware_spread_simulation.py` to start the simulation and observe the network behavior.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This project is intended for educational and research purposes only. Users are responsible for ensuring compliance with applicable laws and regulations before using or modifying the simulation.
