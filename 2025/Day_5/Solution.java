import java.nio.file.*;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;

//The ingredient ID-values are quite large. Mit normalen Zahlen und Listen zu arbeiten wird wahrscheinlich Performance-Probleme geben.

//Erstes Ziel: Zahlen einlesen und prüfen ob int oder long erforderlich ist

public class Solution {

    static ArrayList<long[]> idRanges = new ArrayList<>();
    static ArrayList<Long> idValues = new ArrayList<>(); 
    public static void main(String[] args) throws IOException {
        //List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_5/sampleInput.txt"));
        List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_5/input.txt"));    
        prozessInputLines(lines);
        mergeOverlappingRanges();
        System.out.println("Number of ID ranges: " + idRanges.size());
        System.out.println("Number of ID values: " + idValues.size());
        System.out.println("Number of fresh ingredient IDs: " + countFreshIds());
        System.out.println("Sum of ID ranges: " + sumUpRanges());
    }

    public static long sumUpRanges() {
        return idRanges.stream()
            .mapToLong(range -> range[1] - range[0] + 1)
            .sum();
    }

    //Ziel: Überschneidungsfreie Ranges
    //Methode:  Ranges nach Startwert sortierten, und von vorne nach hinte durchgehen. 
    //          Wenn der Startwert der aktuellen Range kleiner-gleich dem Endwert der vorherigen Range ist, 
    //          den Endwert der vorherigen Range auf den größeren Endwert setzen und die aktuelle Range entfernen.
    public static void mergeOverlappingRanges() {
        idRanges.sort((a, b) -> Long.compare(a[0], b[0]));
        ArrayList<long[]> mergedRanges = new ArrayList<>();
        mergedRanges.add(idRanges.get(0));
        
        for (int i = 1; i < idRanges.size(); i++) {
            long[] currentRange = mergedRanges.get(mergedRanges.size() - 1);
            long[] nextRange = idRanges.get(i);
            if (nextRange[0] <= currentRange[1]) {
                currentRange[1] = Math.max(currentRange[1], nextRange[1]);
            } else {
                mergedRanges.add(nextRange);
            }
        }
        idRanges = mergedRanges;
    }

    public static int countFreshIds() {
        int count = 0;
        for (Long idValue : idValues) {
            if (idIsFresh(idValue)) {
                count++;
            }
        }
        return count;
    }

    public static boolean idIsFresh(long id) {
        for (long[] range : idRanges) {
            if (id >= range[0] && id <= range[1]) {
                return true;
            }
        }
        return false;
    }

    public static void prozessInputLines(List<String> lines) {
        for (String line: lines){
            if (line.contains("-")) {
                String[] parts = line.split("-");
                long start = Long.parseLong(parts[0]);
                long end = Long.parseLong(parts[1]);
                idRanges.add(new long[] {start, end});
            }
            else if (line.length() > 0) {
                long value = Long.parseLong(line);
                idValues.add(value);
            }
        }
    }

}