# Persian Text Plotting Utility

A professional, easy-to-use tool for rendering and displaying Persian (Farsi) text in plots using Python’s Matplotlib, with robust support for right-to-left (RTL) scripts. This project leverages [arabic_reshaper](https://pypi.org/project/arabic-reshaper/) and [python-bidi](https://pypi.org/project/python-bidi/) to ensure accurate display of Persian characters, making it ideal for data visualization, research, and presentation purposes.

---

## Features

- **Seamless Persian Language Support:**  
  Display Persian text accurately in all Matplotlib figures, with correct character joining and bidirectional text rendering.
- **Professional Visualization:**  
  Produce publication-quality plots that incorporate Persian labels, titles, and annotations.
- **Extensible Architecture:**  
  Designed to support future enhancements, such as JSON-based configuration and additional RTL languages.

---

## Installation

Install the required packages via `pip`:

```bash
pip install matplotlib arabic_reshaper python-bidi
```

---

## Usage

Here's how you can use this utility to display Persian text in your Matplotlib plots:

```python
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# Your Persian text
persian_text = "سلام، خوش آمدید!"

# Reshape and apply BiDi algorithm
reshaped_text = arabic_reshaper.reshape(persian_text)
bidi_text = get_display(reshaped_text)

# Create a simple plot with Persian title
plt.plot([1, 2, 3], [4, 5, 6])
plt.title(bidi_text)
plt.xlabel(get_display(arabic_reshaper.reshape("محور افقی")))
plt.ylabel(get_display(arabic_reshaper.reshape("محور عمودی")))
plt.show()
```

---

## Persian Language Support

This project is purpose-built for Persian (Farsi) text, ensuring:

- Proper character connections (reshaping)
- Right-to-left (RTL) layout
- Accurate handling of mixed English/Persian content

If you encounter any rendering issues or have suggestions for supporting other RTL languages, please open an issue or contribute!

---

## Roadmap

- [ ] **JSON Configuration:** Easily manage font settings and text options via external config files.
- [ ] **Multi-language RTL Support:** Extend support for other RTL languages (e.g., Arabic, Urdu).
- [ ] **Enhanced Font Integration:** Simplified font management for Persian and custom fonts.

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request describing your changes. Make sure to follow the [contribution guidelines](CONTRIBUTING.md) if available.

---

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

---

## Acknowledgments

- [Matplotlib](https://matplotlib.org/)
- [arabic_reshaper](https://pypi.org/project/arabic-reshaper/)
- [python-bidi](https://pypi.org/project/python-bidi/)

---

> **Note:** This utility is under active development. Your feedback and feature requests are greatly appreciated!
