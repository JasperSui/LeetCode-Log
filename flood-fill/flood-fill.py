class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        self.dfs(image, sr, sc, m, n, image[sr][sc], newColor)
        return image
    
    def dfs(self, image, i, j, m, n, original_color, new_color):
        if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != original_color or image[i][j] == new_color: return

        image[i][j] = new_color
        
        self.dfs(image, i, j+1, m, n, original_color, new_color)
        self.dfs(image, i, j-1, m, n, original_color, new_color)
        self.dfs(image, i+1, j, m, n, original_color, new_color)
        self.dfs(image, i-1, j, m, n, original_color, new_color)