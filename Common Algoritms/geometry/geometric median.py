def geometric_median(points, tol=1e-5, max_iter=1000):
    """
    Compute the geometric median of a set of 2D points using Weiszfeld's algorithm without NumPy.
    
    Parameters:
        points (list of tuple): A list of 2D points, e.g., [(x1, y1), (x2, y2), ...].
        tol (float): Tolerance for stopping criterion.
        max_iter (int): Maximum number of iterations.
    
    Returns:
        tuple: The geometric median as a 2D point (x, y).
    """
    # Step 1: Initialize with the centroid (arithmetic mean)
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)
    
    for _ in range(max_iter):
        # Step 2: Compute distances to all points
        distances = []
        for px, py in points:
            distance = ((x - px)**2 + (y - py)**2)**0.5
            distances.append(distance)
        
        # Handle zero distance (coinciding point)
        if any(d < 1e-12 for d in distances):
            return points[distances.index(min(distances))]
        
        # Step 3: Update weights (1/distance)
        weighted_sum_x = 0
        weighted_sum_y = 0
        weight_sum = 0
        
        for (px, py), d in zip(points, distances):
            weight = 1 / d
            weighted_sum_x += weight * px
            weighted_sum_y += weight * py
            weight_sum += weight
        
        # Step 4: Compute new estimate
        new_x = weighted_sum_x / weight_sum
        new_y = weighted_sum_y / weight_sum
        
        # Step 5: Check convergence
        if ((new_x - x)**2 + (new_y - y)**2)**0.5 < tol:
            return (new_x, new_y)
        
        # Update for next iteration
        x, y = new_x, new_y
    
    raise ValueError("Weiszfeld's algorithm did not converge within the maximum number of iterations.")

# Example usage
if __name__ == "__main__":
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]
    result = geometric_median(points)
    print(f"Geometric Median: {result}")
