import java.nio.file.*;
import java.io.IOException;
import java.util.List;


public class Solution {
    public static void main(String[] args) throws IOException {
        //List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_3/sampleInput.txt"));
        List<String> lines = Files.readAllLines(Paths.get("c:/Projekte/GitRepos/AdventOfCode/2025/Day_3/input.txt"));        
        solution2(lines);
    }

    public static void solution1(List<String> lines) {
        //Pro Zeile: Erzeuge Bank Objekt und finde maxJoltage. Addiere alle Ergebnisse und gib diese aus.
        long sum = 0;
        for (String line : lines) {
            Bank bank = new Bank(line);
            Long maxJoltage = bank.findMaxJoltage();
            sum += maxJoltage;
        }
        System.out.println("Sum of max joltage values: " + sum);
    }

    public static void solution2(List<String> lines) {
        //Pro Zeile: Erzeuge Bank Objekt und finde maxJoltage. Addiere alle Ergebnisse und gib diese aus.
        //Gebe für jede Zeile maxJoltage aus.
        long sum = 0;
        for (String line : lines) {
            Bank bank = new Bank(line);
            Long maxJoltage = bank.findRecursiveMaxJoltage(bank.input, 12L);
            System.out.println("Max joltage for line " + line + " is: " + maxJoltage);
            sum += maxJoltage;
        }
        System.out.println("Sum of max joltage values: " + sum);
    }
}


public class Bank {

    public List<Long> input;

    public Bank(String input) { 
        //Wandle string in Liste von Longs um. Der String ist nur eine Zeile mit nicht-getrennten Zahlen.
        this.input = input.chars()
            .mapToObj(c -> String.valueOf((char) c))
            .map(Long::parseLong)
            .toList();
    }

    //Aus input muss eine zwölfstellige Zahl result erzeugt werden, welche die größte mögliche darstellt.
    //Jede Ziffer von result muss in input vorkommen und die Reihenfolge der Ziffern in result muss der Reihenfolge in input entsprechen.
    //Input ist immer mindestens zwölf Ziffern lang.
    //Gedanken zum Algorithmus:
    //Der Algorithmus bildet result von links nach rechts und versucht immer die größtmögliche Ziffer an der aktuellen Position zu wählen.
    //Problem: Angenommen wir wollen die ersten Ziffer auswählen und es stehen mehrere 9en zur Verfügung. Welche 9 wählen wir?
    //Da wir nicht wissen, ob wir mit der aktuellen Wahl später eine größere Zahl bilden können, müssen wir alle Möglichkeiten durchprobieren.
    //Dazu verwenden wir Rekursion: Wir wählen eine Ziffer aus, bilden den Rest der Zahl rekursiv und vergleichen die Ergebnisse.
    //Die Funktion sucht auf der Teilliste input[begin:end] die erste größtmögliche Ziffer für die aktuelle Position und ruft sich dann rekursiv auf für die nächste Position mit dem Rest der Liste.
    public Long findRecursiveMaxJoltage(List<Long> input, Long remainingDigits) {
        if (remainingDigits == 1) {
            //Return die größte Ziffer im input
            return input.stream().max(Long::compareTo).orElse(0L);
        }

        //Finde die größte Ziffer im Input inkl. ihrer Position. Dabei muss berücksichtigt werden, dass noch genügend Ziffern für die restlichen Positionen übrig bleiben.
        Long maxNumber = 0L;
        for (int i = 0; i <= input.size() - remainingDigits; i++) {
            Long currentNumber = input.get(i);
            if (currentNumber > maxNumber) {
                maxNumber = currentNumber;
            }
        }
        int maxIndex = input.indexOf(maxNumber);

        //Erzeuge eine Teilliste von input, welche nur die Ziffern hinter der gefundenen maxNumber enthält.
        List<Long> subInput = input.subList(maxIndex + 1, input.size());

        return Long.parseLong(String.valueOf(maxNumber) + findRecursiveMaxJoltage(subInput, remainingDigits - 1));
    }


    public Long findMaxJoltage() {
        //Finde die größte Zahl in der Eingabe welche nicht ganz am Ende steht (a). Finde als nächstes die größte Zahl, welche hinter a steht (b).
        //Erzeuge einen string "ab" und wandle diesen in einen Long um und gib diesen zurück.
        Long maxBeforeLast = input.subList(0, input.size() - 1).stream().max(Long::compareTo).orElse(null);
        Long maxAfterMax = input.subList(input.indexOf(maxBeforeLast) + 1, input.size()).stream().max(Long::compareTo).orElse(null);
        return Long.parseLong(String.valueOf(maxBeforeLast) + String.valueOf(maxAfterMax));
    }
    

    @Override
    public String toString() {
        return "Bank{" +
                "input=" + input +
                '}';
    }
}