import hou

# Get the current network editor and selected nodes
selected_nodes = hou.selectedNodes()

if not selected_nodes:
    hou.ui.displayMessage("Please select at least one node.", severity=hou.severityType.Warning)
else:
    # Get the parent context (e.g., /obj, /out, /shop)
    parent = selected_nodes[0].parent()
    
    # Start an undo block to group all actions into one undo step
    with hou.undos.group("Create Out Nulls"):
        for node in selected_nodes:
            # Create a null node
            out_null = parent.createNode("null")
            
            # Name the null node
            out_null.setName(f"OUT_{node.name()}", unique_name=True)
            
            # Set the color to black
            out_null.setColor(hou.Color((0, 0, 0)))
            
            # Connect it to the selected node
            # Check the first available input on the null
            out_null.setInput(0, node)
            
            # Move it to a tidy position relative to the selected node
            out_null.moveToGoodPosition()

    hou.ui.displayMessage(f"Created and connected {len(selected_nodes)} OUT null(s).")