import java.util.Scanner;
//publicクラスの名前はファイル名と完全に一致していなければなりません
public class HelloWorld_java {
    public static void main(String[] args) {
        //Scannerのインスタンスが必要です
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter your name: ");
        String name = scanner.next();
        System.out.println("Hello, " + name + "!");
        scanner.close();
    }
} 