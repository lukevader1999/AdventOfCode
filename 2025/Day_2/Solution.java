
import java.nio.file.*;
import java.io.IOException;
import java.util.List;

enum InvalidIdMode {
    BY_HALVES,
    BY_REPEATING_SEQUENCE
}

public class Solution {

    public static void main(String[] args) throws IOException {
        //String line = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_2/sampleInput.txt")).getFirst();
        String line = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_2/input.txt")).getFirst();
        List<Range> ranges = convertInput(line);
        solution(ranges, InvalidIdMode.BY_HALVES);
        solution(ranges, InvalidIdMode.BY_REPEATING_SEQUENCE);
    }


    public static void solution(List<Range> ranges, InvalidIdMode mode) {
        long invalidSum = 0;
        System.out.println("\nMode: " + mode);
        for (Range range : ranges) {
            List<Long> invalidIds = range.getInvalidIdsInRange(mode);
            System.out.println("Invalid IDs in range " + range + ": " + invalidIds);
            for (long id : invalidIds) {
                invalidSum += id;
            }
        }
        System.out.println("Sum of invalid IDs: " + invalidSum);
    }

    public static List<Range> convertInput(String line) {
        //Eine Range ist immer im Format "min-max", die Formate sind durch ein , getrennt.
        List<Range> ranges = new java.util.ArrayList<>();
        String[] rangeStrings = line.split(",");
        for (String rangeString : rangeStrings) {
            String[] parts = rangeString.split("-");
            long min = Long.parseLong(parts[0]);
            long max = Long.parseLong(parts[1]);
            ranges.add(new Range(min, max));
        }
        return ranges;
    }
}



class Range {
    long min;
    long max;

    public Range(long min, long max) {
        this.min = min;
        this.max = max;
    }

    public List<Long> getInvalidIdsInRange(InvalidIdMode mode) {
        List<Long> invalidIds = new java.util.ArrayList<>();
        for (long i = min; i <= max; i++) {
            if (isInvalidId(i, mode)) {
                invalidIds.add(i);
            }
        }
        return invalidIds;
    }

    public static boolean isInvalidId(long id, InvalidIdMode mode) {
        String idStr = String.valueOf(id);
        switch (mode) {
            case BY_HALVES:
                return isInvalidIdByHalves(idStr);
            case BY_REPEATING_SEQUENCE:
                return isInvalidIdByRepeatingSequence(idStr);
            default:
                return false;
        }
    }

    public static boolean isInvalidIdByHalves(String id) {
        int length = id.length();
        if (length % 2 != 0) {
            return false;
        }
        String firstHalf = id.substring(0, length / 2);
        String secondHalf = id.substring(length / 2);
        return firstHalf.equals(secondHalf);
    }

    public static boolean isInvalidIdByRepeatingSequence(String id) {
        int length = id.length();
        for (int seqLength = 1; seqLength <= length / 2; seqLength++) {
            if (length % seqLength == 0) {
                String sequence = id.substring(0, seqLength);
                StringBuilder repeated = new StringBuilder();
                int repeatCount = length / seqLength;
                for (int i = 0; i < repeatCount; i++) {
                    repeated.append(sequence);
                }
                if (repeated.toString().equals(id)) {
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public String toString() {
        return "[" + min + "-" + max + "]";
    }
}