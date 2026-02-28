# Fresh Produce Annotation Pipeline

A structured computer vision dataset project focused on multi-class object detection of fresh produce collected from a local market.

This project demonstrates:

- Image dataset organization
- Bounding box annotation using CVAT
- YOLO format export
- Annotation validation using Python
- Version-controlled dataset scaling (Batch-based workflow)

---

## 📌 Project Overview

The dataset contains real-world market images annotated for object detection using the YOLO format.

### 🎯 Target Classes

| Class ID | Class Name |
|----------|------------|
| 0 | Orange |
| 1 | Pepper |
| 2 | Tomato |
| 3 | Onion |

All annotations were created using CVAT and exported in YOLO format.

---

## 📂 Project Structure
fresh-produce-annotation-pipeline/
│
├── annotation_guidelines/
│   └── annotation_rules.md
│
├── data/
│   ├── images/
│   │   ├── batch_1/
│   │   ├── batch_2/
│   │   ├── batch_3/
│   │   └── batch_4/
│   │
│   └── annotations/
│       ├── batch_1_yolo/
│       │   ├── labels/
│       │   └── obj.names
│       │
│       ├── batch_2_yolo/
│       │   ├── labels/
│       │   └── obj.names
│       │
│       ├── batch_3_yolo/
│       │   ├── labels/
│       │   └── obj.names
│       │
│       └── batch_4_yolo/
│           ├── labels/
│           └── obj.names
│
├── notebook/
│   └── count_instances.py
│
├── samples/
│   └── annotated_screenshots/
│       ├── batch_1/
│       ├── batch_2/
│       ├── batch_3/
│       └── batch_4/
│
├── README.md
└── requirements.txt

---

## 📊 Dataset Statistics

### Batch 1
- Images: 100  
- Total Instances: 669  

### Batch 2
- Images: 100  
- Total Instances: 614  

### Batch 3
- Images: 100  
- Total Instances: 593  

### Batch 4
- Images: 89  
- Total Instances: 465  
---

## 📈 Final Combined Dataset Statistics

| Class   | Total Instances |
|----------|----------------|
| Orange   | 330 |
| Pepper   | 840 |
| Tomato   | 549 |
| Onion    | 622 |

**Total Images:** 389  
**Grand Total Instances:** 2,341


## 🛠 Annotation Workflow

1. Images collected from local market.
2. Annotated using CVAT with bounding boxes.
3. Exported in YOLO format.
4. Verified using a custom Python script (`count_instances.py`).
5. Organized into batch-based folder structure for scalability.

---

## 🔍 Annotation Guidelines

Annotation rules and labeling standards are documented in:
annotation_guidelines/annotation_rules.md


These rules ensure consistency across batches.

---

## 🧪 Validation Script

To count object instances per class:

```bash
python notebook/count_instances.py