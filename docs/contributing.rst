========================
Contributing to Isadora
========================

Thank you for your interest in contributing to **Isadora**, the ICAO 1983-compliant International Standard Atmosphere (ISA) Python package. Your contributions help maintain and improve the reliability, accuracy, and usability of the package.

This document outlines the guidelines for contributing code, reporting issues, and suggesting improvements.

Getting Started
---------------

1. **Fork the repository** on GitHub:

   .. code-block:: bash

       git clone https://github.com/techkaduna/isadora.git
       cd isadora
       pip install -e .

2. **Create a feature branch** for your work:

   .. code-block:: bash

       git checkout -b feature/your-feature-name

3. **Write code** following the package's style and architecture.

Code Style and Guidelines
-------------------------

- Use **PEP 8** compliant Python code.
- Docstrings should follow **NumPy/SciPy style**.
- All functions, methods, and classes must be documented.
- Use **type hints** where possible.
- Include **unit tests** for any new functionality.
- Maintain **unit-awareness** in all calculations.
- Preserve **ICAO 1983 compliance** for atmospheric calculations.

Testing Your Changes
-------------------

1. Run the **test suite** to ensure all existing tests pass:

   .. code-block:: bash

       pytest tests/

2. Write **new tests** for added functionality, covering:
   - Atmospheric property calculations
   - Unit conversions
   - Derived quantities (Mach number, dynamic pressure, geometric height)
   - Edge cases and layer boundaries

3. Ensure tests pass in **all supported unit systems**: SI, USCS, Imperial.

Submitting Changes
-----------------

1. **Commit changes** with clear and descriptive messages:

   .. code-block:: bash

       git add .
       git commit -m "Add feature X: detailed explanation"

2. **Push your branch** to your fork:

   .. code-block:: bash

       git push origin feature/your-feature-name

3. Open a **pull request (PR)** on the main repository. Include:
   - Description of the feature or fix
   - Any relevant references or links
   - Screenshots or sample outputs, if applicable
   - Test results

Issue Reporting
---------------

- Use the **GitHub Issues** tracker for bug reports, feature requests, or questions.
- Provide **clear reproduction steps** for bugs.
- Include Python version, operating system, and unit system when relevant.

Community Guidelines
-------------------

- Be respectful and professional.
- Focus on **scientific accuracy and reproducibility**.
- Discuss changes before implementing major structural modifications.
- Encourage collaboration and review among contributors.

License and Intellectual Property
---------------------------------

- Contributions must comply with the **MIT License** of Isadora.
- By contributing, you agree to license your changes under the same license.

Acknowledgements
----------------

- The Isadora logo and documentation were assisted by **ChatGPT**.
- Thank you for helping make Isadora a reliable, ICAO-compliant Python package!
