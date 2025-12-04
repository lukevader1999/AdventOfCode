import java.nio.file.*;
import java.io.IOException;
import java.util.Scanner;

public class SetupNextDay {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter day number: ");
        int day = scanner.nextInt();
        scanner.close();
        String folderName = "Day_" + day;
        Path dayPath = Paths.get("").resolve(folderName);
        try {
            Files.createDirectories(dayPath);
            Files.createFile(dayPath.resolve("input.txt"));
            Files.createFile(dayPath.resolve("sampleInput.txt"));
            Files.createFile(dayPath.resolve("Solution.java"));
            System.out.println("Created folder and files for " + folderName);
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
