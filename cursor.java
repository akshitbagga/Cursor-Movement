import java.awt.Robot;
import java.awt.AWTException;

public class AutoCursorMover {
    public static void main(String[] args) {
        try {
            Robot robot = new Robot();

            // Move the mouse slightly 5 times
            for (int i = 0; i < 5; i++) {
                int x = 500 + (i * 10);
                int y = 300 + (i * 10);
                robot.mouseMove(x, y);
                System.out.println("Moved to (" + x + "," + y + ")");
                Thread.sleep(1000); // Wait 1 second
            }

        } catch (AWTException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
