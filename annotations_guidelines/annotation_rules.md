# Annotation Guidelines – Local Market Produce Dataset

## Purpose
These guidelines define the rules for annotating **fresh produce images** collected from local markets.  
The goal is to ensure **consistent, high-quality bounding boxes** for four classes: **orange, pepper, tomato, and onion**.

---

## Classes

| Class ID | Class Name |
|----------|------------|
| 0        | Orange     |
| 1        | Pepper     |
| 2        | Tomato     |
| 3        | Onion      |

> Class IDs correspond to the YOLO `.txt` annotation format.

---

## General Annotation Rules

1. **Bounding Box Placement**
   - Draw boxes **tightly around each object** without cutting edges.  
   - Avoid including unrelated objects inside the bounding box.  

2. **Partial Visibility**
   - Annotate objects only if **at least 40% of the object is visible**.  
   - Objects mostly blocked or obscured by trays, hands, or packaging should be skipped.  

3. **Overlapping Objects**
   - Annotate **every object individually**, even if partially overlapping.  
   - Do not merge overlapping objects into a single bounding box.  

4. **Packaged Produce**
   - For objects in **nylon bags, trays, or containers**:  
     - Label only **fully visible produce**.  
     - Skip objects mostly hidden by packaging.  

5. **Multi-class Images**
   - Each object must be labeled with the **correct class ID**.  
   - Multiple classes in one image are allowed.  

6. **Multiple Instances of the Same Class**
   - Each object instance gets a **separate bounding box**, even if they are adjacent or touching.  

7. **Exclusions**
   - Damaged or rotten produce should **not** be annotated.  
   - Objects outside the main focus area of the image can be ignored.  

---

## File Naming & Structure

- **Image files**: Keep original filenames.  
- **YOLO annotation files**: Must have the **same name** as the corresponding image but with `.txt` extension.  
- **Class IDs**: Must match `obj.names` file.  

Example:

```text
image001.jpg
image001.txt  ← annotations