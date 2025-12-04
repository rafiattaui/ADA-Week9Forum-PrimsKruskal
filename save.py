def save_to_csv(graph_name, primsMst, total_weight, execution_time, filename="kruskal_output.csv"):
    import csv

    # Check for existing headers
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers if file is empty
        file.seek(0, 2)  # Move to end of file
        if file.tell() == 0:
            writer.writerow(["Graph Name", "Total Weight", "Kruskal Execution Time (s)", "Vertices", "Edges"])
        
        writer.writerow([graph_name, total_weight, execution_time, len(primsMst) + 1, len(primsMst)])
        
        