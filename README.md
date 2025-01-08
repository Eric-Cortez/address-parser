# Sonic Software Engineer Application

## Address Parser

### Overview

Address Parser is a tool developed as part of my application for the Sonic Software Engineer position. It extracts standard components from address strings, such as recipient, street, city, state, and ZIP code.

> **Note:** This parser is currently designed for U.S.-based addresses.

### Features

- Extracts recipient, street address, city, state, and ZIP code.
- Includes test cases for validation.

Example Input:

```
    Sonic
    2260 Apollo Way
    Santa Rosa, CA 95407
```

Example Output:

```
    {
    "recipient": "Sonic",
    "street_address": "2260 Apollo Way",
    "city": "Santa Rosa",
    "state": "CA",
    "zip_code": "95407",
    }
```

## Setup

1. Clone the repository:

   ```bash
        git clone https://github.com/Eric-Cortez/address-parser.git
        cd address-parser
   ```

2. Create a virtual environment (optional):

   ```bash
        python -m venv venv
        source venv/bin/activate  # macOS/Linux
        venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
        pip install -r requirements.txt
   ```

## Running Tests

Run all tests:
   ```bash
        pytest
   ```

## Question:

Parse Sonic's main address as it would appear on an envelope into standard components. List the difficulties faced when figuring out address structure.

### Answer:

To parse Sonic’s main address into standard components, we would identify the following parts:

1. Recipient: Sonic
2. Street Address: 2260 Apollo Way
3. City: Santa Rosa
4. State: CA
5. ZIP Code: 95407

### Difficulties faced when figuring out address structure:

1. **Inconsistent Formatting:** Addresses can vary significantly in structure. Some may include unit numbers, suite numbers, or P.O. Boxes, which complicate parsing.
2. **Abbreviations:** Common abbreviations like "St." for "Street" or "Ave." for "Avenue" can be confusing.
3. **Missing Components:** Sometimes, an address might be missing a ZIP code or even the recipient's name, requiring assumptions or defaults.
4. **Multiline vs. Single-line Input:** Addresses can appear in one line or multiple lines, so the parser needs to handle both types.
5. **Edge Cases:** While this implementation focuses on parsing standard address formats, there are several edge cases that would require additional handling, such as invalid or incomplete addresses, missing components (e.g., ZIP code or city), or non-standard formats. These cases are important to consider for a more robust solution in future iterations.
