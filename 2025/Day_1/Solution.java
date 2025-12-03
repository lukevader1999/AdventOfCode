import java.nio.file.*;
import java.io.IOException;
import java.util.List;

public class Solution {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_1/input.txt"));
        //List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_1/sampleInput.txt"));
        //solution1(lines);
        solution2(lines);
    }

    public static void solution1(List<String> lines) {
        int startValue = 50;
        int counter = 0;

        for (String el : lines) {
            startValue = realMod(startValue + convertToInt(el), 100);
            System.out.println("Current Value: " + startValue);
            if (startValue == 0) {
                counter++;
            }
        }
        System.out.println("Counter: " + counter);
    }

    public static void solution2(List<String> lines) {
        int startValue = 50;
        int counter = 0;

        for (String el : lines) {
            System.out.println("Current Value: " + startValue);
            int rotationSteps = convertToInt(el);
            System.out.println("Rotation Steps: " + rotationSteps);
            counter += countZerosinRotation(startValue, rotationSteps);
            startValue = realMod(startValue + rotationSteps, 100);
            System.out.println("Current Counter: " + counter);
        }
        System.out.println("Counter: " + counter);
    }

    public static int convertToInt(String s) {
        int sign = s.charAt(0) == 'R' ? 1 : -1;
        return Integer.parseInt(s.substring(1)) * sign;
    }

    public static int realMod(int value, int base) {
        return ((value % base) + base) % base;
    }

    public static int countZerosinRotation(int startPosition, int rotationSteps) {
        //Assumptions: startPosition between 0 and 99, rotationSteps cant be zero
        int endPosition = startPosition + rotationSteps;
        if (endPosition > 0){
            return endPosition / 100;
        }
        else { //endPosition < 0
            if (startPosition == 0) {
                return (-endPosition/100);
            }
            return 1 + (-endPosition/100);
        }
    }
}