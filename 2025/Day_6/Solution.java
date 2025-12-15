import java.nio.file.*;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Solution {

    static ArrayList<Problem> problemsList = new ArrayList<>();
    static List<String> lines;

    public static void main(String[] args) throws IOException {
        //lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_6/sampleInput.txt"));
        lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_6/input.txt"));    
        //prozessInputLines(lines);     //First part
        initProblemsListWithColums();   //Second part
        Long finalResult = computeFinalResult();
        System.out.println("Final result: " + finalResult);
    }

    public static void initProblemsListWithColums(){
        int lastStartIndex = 0;
        for(int i = 0; i < lines.get(0).length(); i++) {
            if (!isEmptyColumn(i)) {
                continue;
            }
            List<String> column = getColumn(lastStartIndex, i);
            Problem problem = new Problem();
            problem.setNumbersWithColumn(column);
            problemsList.add(problem);
            lastStartIndex = i + 1;
        }

        List<String> column = getColumn(lastStartIndex, lines.get(0).length());
        Problem problem = new Problem();
        problem.setNumbersWithColumn(column);
        problemsList.add(problem);
    }

    public static List<String> getColumn(int startIndex, int endIndex) {
        List<String> column = new ArrayList<>();
        for (String line : lines) {
            column.add(line.substring(startIndex, endIndex));
        }
        return column;
    }

    public static boolean isEmptyColumn(int colIndex) {
        for (String line : lines) {
            if (line.charAt(colIndex) != ' ') {
                return false;
            }
        }
        return true;
    }

    public static Long computeFinalResult() {
        Long finalResult = 0L;
        for (Problem problem : problemsList) {
            finalResult += problem.computeResult();
        }
        return finalResult;
    }

    public static void prozessInputLines(List<String> lines) {
        processFirstLine(lines.get(0));
        for (int i = 1; i < lines.size()-1; i++) {
                processNumberLine(lines.get(i));
        }
        processOperatorLine(lines.get(lines.size()-1));
    }

    static void processFirstLine(String line) {
        List<Integer> numbers = Arrays.stream(line.split("\\s+"))
            .filter(s -> s != "")
            .map(Integer::parseInt)
            .toList();
        for(int i = 0; i < numbers.size(); i++) {
            Problem problem = new Problem();
            problem.addNumber(numbers.get(i));
            problemsList.add(problem);
        }
    }

    static void processNumberLine(String line) {
        List<Integer> numbers = Arrays.stream(line.split("\\s+"))
            .filter(s -> s != "")
            .map(Integer::parseInt)
            .toList();
        for(int i = 0; i < numbers.size(); i++) {
            problemsList.get(i).addNumber(numbers.get(i));
        }
    }

    static void processOperatorLine(String line) {
        List<String> operators = Arrays.stream(line.split("\\s+"))
            .toList();
        for(int i = 0; i < operators.size(); i++) {
            problemsList.get(i).setOperator(operators.get(i));
        }
    }
}

class Problem {

    static List<String> validOperators = List.of("+", "*");

    public ArrayList<Integer> numbers = new ArrayList<>();
    public String Operator = "";

    public void setNumbersWithColumn(List<String> column) {
        System.out.println("Setting numbers with column: " + column);
        this.setOperator(column.get(column.size() - 1));
        column.remove(column.size() - 1);
        for (int i = 0; i < column.get(0).length(); i++) {
            this.addNumber(createNumberFromIndex(column, i));
        }
        System.out.println("Numbers: " + this.numbers + ", Operator: " + this.Operator);
    }

    public Integer createNumberFromIndex(List<String> column, int index) {
        validateColumn(column);

        String numberString = "";
        for (int i = 0; i < column.size(); i++) {
            numberString += column.get(i).charAt(index);
        }
        numberString = numberString.trim();
        return Integer.parseInt(numberString);
    }

    public void validateColumn(List<String> column) {
        int length = column.get(0).length();
        for (String line : column) {
            if (line.length() != length) {
                throw new IllegalArgumentException("Inconsistent line lengths in column: " + column);
            }
        }
    }

    public void setOperator(String value) {
        value = value.trim();
        if (validOperators.contains(value)) {
            this.Operator = value;
        } else {
            throw new IllegalArgumentException("Invalid operator: " + value);
        }
    }

    public void addNumber(int number) {
        this.numbers.add(number);
    }

    public Long computeResult() {
        Long result = 0L;
        if (this.Operator.equals("+")) {
            for (Integer number : this.numbers) {
                result += number;
            }
        } else if (this.Operator.equals("*")) {
            result = 1L;
            for (Integer number : this.numbers) {
                result *= number;
            }
        } else {
            throw new IllegalStateException("Operator not set or invalid: " + this.Operator);
        }
        return result;
    }
}
