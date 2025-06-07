# PhoenixPing

PhoenixPing is a powerful and user-friendly network monitoring tool designed to track the status of multiple IP addresses in real-time. Built with Python, it provides a live graphical visualization of network connectivity using Matplotlib, with full support for Persian (Farsi) language in the user interface. Whether you're a network administrator, a developer, or an enthusiast, PhoenixPing offers a seamless way to monitor network health, log results, and troubleshoot connectivity issues.

![PhoenixPing Screenshot](screenshots/sample.png)

---

## Features

- **Real-time Monitoring:** Continuously pings specified IP addresses and displays their status (online/offline) in a live Matplotlib graph.
- **Multi-IP Support:** Monitor multiple IP addresses simultaneously, with distinct visual representations for each.
- **Persian Language Support:** Fully localized UI with Persian labels and text, powered by `arabic_reshaper` and `bidi`.
- **Cross-Platform Compatibility:** Works on Windows, Linux, and macOS with automatic platform detection for ping commands.
- **Efficient Memory Usage:** Uses `collections.deque` to manage memory efficiently, ensuring smooth performance during long-term monitoring.
- **Logging:** Saves ping results with timestamps to a CSV file (`ping_log.csv`) for post-analysis.
- **Error Handling:** Robust validation of IP addresses and error management for reliable operation.
- **Customizable Settings:** Configurable ping interval and display window size for flexible monitoring.
- **Safe Shutdown:** Gracefully handles program termination to prevent resource leaks.

---

## Prerequisites

To run PhoenixPing, ensure you have the following installed:

- **Python 3.6+**

### Required Python packages:

```bash
pip install matplotlib arabic_reshaper python-bidi
```

- A system with the `ping` command available (pre-installed on Windows, Linux, and macOS).

---

## Installation

### Clone the Repository:

```bash
git clone https://github.com/<your-username>/PhoenixPing.git
cd PhoenixPing
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, install the required packages manually:

```bash
pip install matplotlib arabic_reshaper python-bidi
```

### Run the Program:

```bash
python phoenix_ping.py
```

---

## Usage

### Launch PhoenixPing

Run the script using Python:

```bash
python phoenix_ping.py
```

### Enter IP Addresses

A dialog box will prompt you to enter IP addresses, separated by commas (e.g., `192.168.1.1,8.8.8.8`).

- Invalid IPs will be filtered out, and an error message will appear if no valid IPs are provided.

### View Real-time Graph

- A live Matplotlib graph displays the status of each IP address (Online: 1, Offline: 0).
- Each IP is represented by a distinct colored line with markers for clarity.
- The x-axis shows time (in seconds), and the y-axis indicates connectivity status (Online/Offline).
- The graph automatically scrolls to show the most recent `max_display_time` data points (default: 100 seconds).

### Check Logs

Ping results are saved in `ping_log.csv` with timestamps and status for each IP.

**Example log format:**

```csv
Timestamp,192.168.1.1,8.8.8.8
2025-06-07 10:30:45.123456,True,True
2025-06-07 10:30:46.123456,True,False
```

### Stop the Program

- Close the Matplotlib window to safely terminate the program.
- All threads are gracefully stopped, and resources are released.

---

## Configuration

PhoenixPing includes customizable settings in the code. Modify the `config` dictionary in `phoenix_ping.py` to adjust:

- `ping_interval`: Time between pings (in seconds, default: 1).
- `max_display_time`: Number of data points shown in the graph (default: 100).

**Example:**

```python
config = {
    "ping_interval": 1,  # Ping every 1 second
    "max_display_time": 100  # Show last 100 seconds of data
}
```

*Future versions may support loading configurations from a JSON file.*

---

## Screenshots

**Live Graph Example:**  
Real-time visualization of IP status with Persian labels.

![Live Graph Example](screenshots/sample.png)

---

## Contributing

We welcome contributions to make PhoenixPing even better! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines and includes appropriate tests.

---

## Issues and Support

If you encounter any issues or have suggestions, please:

- Open an issue on the [GitHub Issues](../../issues) page.
- Provide detailed information about the problem, including your operating system, Python version, and any error messages.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built with [Matplotlib](https://matplotlib.org/) for visualization.
- Persian text support powered by [arabic_reshaper](https://github.com/mpcabd/python-arabic-reshaper) and [python-bidi](https://github.com/MeirKriheli/python-bidi).
- Inspired by the need for a simple, localized network monitoring tool.

---

## Contact

For questions or feedback, reach out via GitHub Issues or connect with the community on X.

---

**PhoenixPing** – Monitor your network with ease, visualize with clarity, and stay connected!

---

## Notes

- **Placeholder:** Replace `<your-username>` in the URLs with your actual GitHub username.
- **Screenshots:** The README references a `screenshots/sample.png` file. You’ll need to create and upload a screenshot of the running program (e.g., the Matplotlib graph) to the `screenshots` folder in your repository.
- **License File:** Create a LICENSE file in your repository with the MIT License text (or another license of your choice).
- **Requirements File:** Create a `requirements.txt` file with:

    ```
    matplotlib
    arabic_reshaper
    python-bidi
    ```

---
