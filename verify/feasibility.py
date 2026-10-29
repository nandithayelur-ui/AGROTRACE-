from typing import Dict, List, Any

def check_allocation_feasibility(
    lots: List[Dict[str, Any]],
    contract: Dict[str, Any],
    allocation_map: Dict[int, int]
) -> Dict[str, Any]:
    violations = []
    total_assigned_g = 0
    assigned_lot_ids = set()

    contract_id = contract.get("id", 1)
    min_grade = contract.get("min_grade", 1)
    capacity_g = contract.get("qty_g", 0)

    lots_by_id = {l["id"]: l for l in lots}

    for lot_id, assign_weight in allocation_map.items():
        if assign_weight <= 0:
            continue

        if lot_id in assigned_lot_ids:
            violations.append(f"Lot {lot_id} duplicate assignment in payload")
        assigned_lot_ids.add(lot_id)

        lot = lots_by_id.get(lot_id)
        if not lot:
            violations.append(f"Lot {lot_id} does not exist in candidate pool")
            continue

        grade = lot.get("grade", 0)
        if grade < min_grade:
            violations.append(f"Lot {lot_id} grade {grade} is below contract minimum {min_grade}")

        avail_weight = lot.get("weight_g", 0) - lot.get("allocated_weight_g", 0)
        if assign_weight > avail_weight:
            violations.append(f"Lot {lot_id} assigned {assign_weight}g exceeds available {avail_weight}g")

        total_assigned_g += assign_weight

    if total_assigned_g > capacity_g:
        violations.append(f"Total allocation {total_assigned_g}g exceeds contract capacity {capacity_g}g")

    is_feasible = (len(violations) == 0 and total_assigned_g > 0)
    return {
        "feasible": is_feasible,
        "contract_id": contract_id,
        "total_assigned_g": total_assigned_g,
        "capacity_g": capacity_g,
        "lots_used_count": len(assigned_lot_ids),
        "violations": violations
    }
