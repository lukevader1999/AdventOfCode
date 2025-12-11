import java.nio.file.*;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;


public class Solution {

    static ArrayList<ArrayList<Boolean>> grid;

    public static void main(String[] args) throws IOException {
        //List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_4/sampleInput.txt"));
        List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_4/input.txt"));        
        grid = linesToGrid(lines);
        System.out.println(countAndRemoveLopp());
    }

    public static int countAndRemoveLopp() {
        int totalCount = 0;
        while (true) {
            int count = countAndRemoveAccesibles();
            if (count == 0) {
                break;
            }
            totalCount += count;
        }
        return totalCount;
    }

    public static int countAndRemoveAccesibles() {
        //Iteriere über alle Zellen im Grid und zähle die Anzahl der zugänglichen Zellen.
        int count = 0;
        for (int y = 0; y < grid.size(); y++) {
            for (int x = 0; x < grid.get(y).size(); x++) {
                if (isAccesible(x, y)) {
                    count++;   
                    grid.get(y).set(x, false);
                }
            }
        }
        return count;
    }

    public static boolean isAccesible(int x, int y) {
        if (x < 0 || y < 0 || y >= grid.size() || x >= grid.get(y).size()) {
            return false;
        }
        if (grid.get(y).get(x) == false) {
            return false;
        }
        
        int countTrueNeighbors = 0;
        int[][] directions = { {0, -1}, {0, 1}, {-1, 0}, {1, 0} , {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };
        for (int[] dir : directions) {
            int newX = x + dir[0];
            int newY = y + dir[1];
            if (newX >= 0 && newY >= 0 && newY < grid.size() && newX < grid.get(newY).size()) {
                if (grid.get(newY).get(newX) == true) {
                    countTrueNeighbors++;
                }
            }
        }
        if (countTrueNeighbors <= 3) {
            return true;
        }
        return false;
    }

    public static void printGrid(ArrayList<ArrayList<Boolean>> grid) {
        for (ArrayList<Boolean> row : grid) {
            for (Boolean cell : row) {
                if (cell) {
                    System.out.print("@");
                } else {
                    System.out.print(".");
                }
            }
            System.out.println();
        }
    }

    public static ArrayList<ArrayList<Boolean>> linesToGrid(List<String> lines) {
        ArrayList<ArrayList<Boolean>> grid = new ArrayList<ArrayList<Boolean>>();
        for (String line : lines) {
            ArrayList<Boolean> row = new ArrayList<Boolean>();
            for (char c : line.toCharArray()) {
                if (c == '.') {
                    row.add(false);
                } else if (c == '@') {
                    row.add(true);
                }   
            }
            grid.add(row);
        }
        return grid;
    }

}