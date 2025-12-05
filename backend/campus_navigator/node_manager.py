from .node import Node
from .edge import Edge
import tkinter as tk
from tkinter import messagebox
import random

from heapq import heappush, heappop

class NodeManager:
    def __init__(self,canvas,output_canvas):
        self.output_canvas = output_canvas
        self.canvas = canvas
        self.nodes = []
        self.selected_nodes = []
        self.edges = []
        self.selected_edges = []
        self.bfs_edges = []
        self.dfs_edges = []
        self.closed_edges = []
        self.open_edges = []
        self.non_accesible_edges = []
        self.accessible_only_mode = tk.BooleanVar()

    def create_node(self,x,y,name="Node"):
        node = Node(self.canvas,x,y,name,manager=self)
        print(f"The node {name} has been created at {x},{y}")
        self.nodes.append(node)
        self.canvas.tag_raise("node")
        self.display_output(f"{node.text} has been created at ({x},{y}) with color: {node.original_color}")
    
    def select(self,node):
        if node not in self.selected_nodes:
            self.selected_nodes.append(node)
        self.display_output(f"{node.text} has been selected")

    def deselect(self,node):
        if node in self.selected_nodes:
            self.selected_nodes.remove(node)
            self.canvas.itemconfig(node.rect, fill=node.original_color)
            node.selected = False
        print(node,"has been deselected")
        self.display_output(f"{node.text} has been deselected")

    def create_edge(self, distance, time, accesible=True):
        if len(self.selected_nodes) != 2:
            print("2 nodes need to be selected")
            return
        first_node,second_node = self.selected_nodes
        edge = Edge(self.canvas, first_node, second_node, distance, time, accesible)
        self.edges.append(edge)
        edge.update_state()

        print(f"Edge created between {first_node} and {second_node}")
        self.deselect(first_node)
        self.deselect(second_node)
        self.display_output(f"Edge added: {first_node.text}  ↔ {second_node.text} ({distance}m, {time}min), accesible = {accesible}")
        self.canvas.tag_raise("node")



    def display_output(self,message):
        self.output_canvas.delete("all")
        self.output_canvas.create_text(
            10,10, anchor="nw", text=message,fill="white",font=("Helvectica",10, "bold")
        )

    def randomize_weights(self):
        if not self.edges:
            messagebox.showerror("Empty","No edges available")
        for edge in self.edges:
            edge.distance = random.randint(1,100)
            edge.time = random.randint(1,30)
            self.canvas.itemconfig(edge.label, text=f"{edge.distance}m, {edge.time}min")
        print("Edge weights randomized")
        self.display_output("Edge weights have been randomized")
    
    def restart(self):
        response = messagebox.askquestion("Are you sure?", "Would you like to proceed?")

        if response == "yes":
            for node in self.nodes:
                self.canvas.delete(node.rect)
                self.canvas.delete(node.text_item)
            for edge in self.edges:
                self.canvas.delete(edge.line)
                self.canvas.delete(edge.label)
            
            self.nodes.clear()
            self.selected_nodes.clear()
            self.edges.clear()
            self.selected_edges.clear()

            print("Canvas and graph reset.")
        else:
            return

    def dfs(self, start_name, goal_name):
        for edge in self.edges:
            edge.update_state()
        start = next((n for n in self.nodes if n.text == start_name), None)
        goal = next((n for n in self.nodes if n.text == goal_name), None)

        if not start or not goal:
            messagebox.showerror("Invalid", "Start or goal node not found.")
            return

        # Optional: reset edge colors before traversal
        for edge in self.edges:
            edge.update_state()

        visited = set()
        stack = [(start, [], [start])]  # (current_node, path_edges, path_nodes)

        while stack:
            current, path_edges, path_nodes = stack.pop()
            if current in visited:
                continue
            visited.add(current)

            self.canvas.update()
            self.canvas.after(100)

            if current == goal:
                total_distance = sum(edge.distance for edge in path_edges)
                total_time = sum(edge.time for edge in path_edges)

                for edge in path_edges:
                    self.canvas.itemconfig(edge.line, fill="green")
                self.display_output(
                    f"Path: {' → '.join(n.text for n in path_nodes)}\n"
                    f"Length: {len(path_edges)} edges\n"
                    f"Total Distance: {total_distance}m\n"
                    f"Total Time: {total_time}min")
                return

            for edge in self.get_connected_edges(current):
                neighbor = edge.second_node if edge.first_node == current else edge.first_node
                if neighbor not in visited:
                    stack.append((neighbor, path_edges + [edge], path_nodes + [neighbor]))

        messagebox.showinfo("No Path", "No path found.")

    def dijkstra(self, start_name, goal_name):
        for edge in self.edges:
            edge.update_state()

        start = next((n for n in self.nodes if n.text == start_name), None)
        goal = next((n for n in self.nodes if n.text == goal_name), None)

        if not start or not goal:
            messagebox.showerror("Invalid", "Start or goal node not found.")
            return

        pq = [(0, start, [], [start])]  # (current_dist, current_node, path_edges, path_nodes)
        visited = set()

        while pq:
            current_dist, current, path_edges, path_nodes = heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            # Goal reached
            if current == goal:
                total_time = sum(edge.time for edge in path_edges)
                for edge in path_edges:
                    self.canvas.itemconfig(edge.line, fill="green")
                self.display_output(
                    f"Dijkstra Path: {' → '.join(n.text for n in path_nodes)}\n"
                    f"Total Distance: {current_dist}m\n"
                    f"Total Time: {total_time}min"
                )
                return

            # Explore neighbors
            for edge in self.get_connected_edges(current):
                neighbor = edge.second_node if edge.first_node == current else edge.first_node
                if neighbor not in visited:
                    heappush(pq, (current_dist + edge.distance,
                                neighbor,
                                path_edges + [edge],
                                path_nodes + [neighbor]))

        messagebox.showinfo("No Path", "No path found.")

    def prim_mst(self):
        if not self.nodes:
            messagebox.showerror("Empty", "No nodes available.")
            return

        visited = set()
        mst_edges = []
        total_distance = 0

        # Start from the first node
        start = self.nodes[0]
        visited.add(start)

        # Priority queue of edges (distance, tie-breaker, edge)
        pq = []
        for edge in self.get_connected_edges(start):
            heappush(pq, (edge.distance, id(edge), edge))

        while pq and len(visited) < len(self.nodes):
            dist, _, edge = heappop(pq)

            u, v = edge.first_node, edge.second_node

            # Skip if both nodes already visited
            if u in visited and v in visited:
                continue

            # Add edge to MST
            mst_edges.append(edge)
            total_distance += dist

            # Pick the new node
            new_node = v if u in visited else u
            visited.add(new_node)

            # Push edges from the new node
            for next_edge in self.get_connected_edges(new_node):
                neighbor = (
                    next_edge.second_node
                    if next_edge.first_node == new_node
                    else next_edge.first_node
                )
                if neighbor not in visited:
                    heappush(pq, (next_edge.distance, id(next_edge), next_edge))

        if len(visited) < len(self.nodes):
            messagebox.showwarning(
                "Disconnected Graph",
                "MST could not include all nodes (graph is disconnected)."
            )

        # Highlight MST edges
        for edge in mst_edges:
            self.canvas.itemconfig(edge.line, fill="blue")

        self.display_output(
            f"MST built with {len(mst_edges)} edges\n"
            f"Total Distance: {total_distance}m"
        )



            
    def bfs(self, start_name, goal_name):
        for edge in self.edges:
            edge.update_state()
        start = next((n for n in self.nodes if n.text == start_name), None)
        goal = next((n for n in self.nodes if n.text == goal_name), None)

        if not start or not goal:
            messagebox.showerror("Invalid", "Start or goal node not found.")
            return

        visited = set()
        queue = [(start, [],[start])]  # Each item: (current_node, path_edges)

        while queue:
            current, path_edges, path_nodes = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)

            self.canvas.update()
            self.canvas.after(100)

            if current == goal:
                total_distance = sum(edge.distance for edge in path_edges)
                total_time = sum(edge.time for edge in path_edges)
                for edge in path_edges:
                    self.canvas.itemconfig(edge.line, fill="green")
                self.display_output(
                    f"Path: {' → '.join(n.text for n in path_nodes)}\n"
                    f"Length: {len(path_edges)} edges\n"
                    f"Total Distance: {total_distance}m\n"
                    f"Total Time: {total_time}min")
                return

            for edge in self.get_connected_edges(current):
                neighbor = edge.second_node if edge.first_node == current else edge.first_node
                if neighbor not in visited:
                    queue.append((neighbor, path_edges + [edge], path_nodes + [neighbor]))

        messagebox.showinfo("No Path", "No path found.")


    def get_neighbors(self,node):
        neighbors = []
        for edge in self.edges:
            if not edge.open:
                continue
            if self.accessible_only_mode.get() and not edge.accessible:
                continue
            if edge.first_node == node:
                neighbors.append(edge.second_node)
            elif edge.second_node == node:
                neighbors.append(edge.first_node)

        return neighbors
    
    def get_connected_edges(self, node):
        edges = []
        for edge in self.edges:
            if not edge.open:
                continue
            if self.accessible_only_mode.get() and not edge.accessible:
                continue
            if edge.first_node == node or edge.second_node == node:
                edges.append(edge)
        return edges