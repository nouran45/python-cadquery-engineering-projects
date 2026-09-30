# Python CadQuery Engineering Projects

A portfolio of parametric CAD models developed using **Python and CadQuery**.

This repository documents my progression from fundamental CadQuery operations to multi-stage engineering modeling, geometric feature creation, repeated patterns, model modification, debugging, and STL generation.

Rather than presenting only finished models, the repository preserves intermediate development stages to demonstrate the engineering and problem-solving process behind each result.

---

## Technologies

- Python
- CadQuery
- Parametric CAD Modeling
- Computational Geometry
- Boolean Operations
- Workplanes and Selectors
- 3D Transformations
- STL Generation
- Engineering Model Debugging

---

## Repository Structure

```text
python-cadquery-engineering-projects/
│
├── learning-exercises/
│   ├── debugging/
│   └── outputs/
│
├── projects/
│   ├── task-1/
│   │   ├── stages/
│   │   ├── final/
│   │   └── renders/
│   │
│   ├── task-2/
│   │   ├── stages/
│   │   ├── final/
│   │   └── renders/
│   │
│   ├── task-3/
│   │   ├── original/
│   │   ├── modified/
│   │   └── renders/
│   │
│   └── task-4/
│       ├── final/
│       └── renders/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Learning Exercises

The `learning-exercises` directory contains smaller models developed while learning the CadQuery workflow.

Topics covered include:

- Basic boxes and primitives
- Cylinders and holes
- Multiple-hole patterns
- Parameterized geometry
- Cylindrical cutouts
- Custom profiles
- Sketching and extrusion
- Boolean union and subtraction
- Rounded geometry
- Shell operations
- Loft operations
- Workplanes
- Selectors
- Translation, rotation, and mirroring
- STL exporting
- Debugging CadQuery geometry

These exercises provided the foundation for the larger engineering tasks in the `projects` directory.

---

# Engineering Projects

## Task 1 — Parametric Tray with Multiple Openings

Task 1 demonstrates progressive construction of a rounded tray-like component.

### Development Stages

#### Stage 1 — Base and Perimeter

Initial outer geometry and perimeter development.

#### Stage 2 — Rounded Internal Cavity

Introduced the internal cavity and rounded internal geometry.

#### Stage 3 — Circular Openings

Refined the model to the required overall dimensions and added:

- Circular side-wall opening
- Circular floor opening

#### Stage 4 — Rectangular Openings

Added the remaining geometric features:

- Rounded rectangular floor opening
- Centered rectangular floor opening
- Rectangular side-wall opening

The final model combines the complete outer body, cavity, circular openings, and rectangular openings.

---

## Task 2 — Repeated Parametric Feature Model

Task 2 demonstrates a more complex staged modeling workflow.

### Development Stages

1. Main base body
2. Outer body geometry
3. Circular opening
4. Hollow-body development
5. Repeated feature generation
6. Raised five-point star features

The final model contains **24 repeated feature positions**, demonstrating how repeated geometry can be generated programmatically instead of manually modeling each feature.

The project also includes the final exported STL model.

---

## Task 3 — Existing Model Modification

Task 3 focuses on modifying an existing parametric model rather than building a component entirely from scratch.

The repository preserves both:

```text
original/
modified/
```

This provides a clear before-and-after representation of the engineering changes.

The project demonstrates:

- Understanding existing CadQuery code
- Modifying parameterized geometry
- Changing geometric proportions
- Creating additional geometric features
- Using polygon-based geometry
- Refining features using fillets
- Exporting the modified model to STL

---

## Task 4 — CadQuery Debugging

Task 4 focuses on diagnosing and correcting a non-working CadQuery model.

The task involved debugging modeling logic and producing a functional final script.

This demonstrates an important engineering programming skill: not only creating CAD geometry, but also understanding and repairing existing parametric CAD code.

---

# Engineering Workflow

The projects demonstrate the following workflow:

```text
Reference Geometry
        ↓
Dimension Analysis
        ↓
Parameterized Model
        ↓
Feature Construction
        ↓
Boolean Operations
        ↓
Workplane / Coordinate Management
        ↓
Debugging and Refinement
        ↓
Final Geometry
        ↓
STL Export
```

---

# Running the Models

Install the required Python dependency:

```bash
pip install -r requirements.txt
```

The scripts are designed for use with a CadQuery-compatible Python environment such as **CQ-editor**.

Example:

```python
import cadquery as cq

model = cq.Workplane("XY").box(20, 10, 5)

show_object(model)
```

---

# Project Goals

This repository documents practical experience with:

- Parametric engineering design
- Python-based CAD automation
- Computational geometry
- Iterative model development
- Geometric problem solving
- Engineering scripting
- Debugging
- 3D model generation

The staged project structure intentionally preserves the development process rather than showing only the finished results.

---

## Future Improvements

Planned improvements include:

- Adding rendered screenshots for each project stage
- Adding final-model previews to the project documentation
- Improving parameter organization and reusable functions
- Adding additional STL exports
- Expanding the collection with more complex parametric CAD projects

---

## Author

**Farida Elselmy**

Computer Engineering student with interests in software development, engineering automation, parametric modeling, and computational design.