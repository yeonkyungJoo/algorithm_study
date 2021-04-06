package leegijin;

public class p_이진변환반복하기 {
    public static void main(String[] args) {
        String s ="110010101001";
        int [] answer =solution(s);
        System.out.println("answer = " + answer[0]+","+answer[1]);
    }
    public static int[] solution(String s) {
        int zeroCount = 0;
        int transformationCount = 0;
        String binary = s;

        while (!"1".equals(binary)) {
            String binaryWithZero = binary.replaceAll("0", "");
            zeroCount += binary.length() - binaryWithZero.length();
            int transformationSize = binaryWithZero.length();
            binary = Integer.toBinaryString(transformationSize);
            transformationCount++;
        }

        return new int[] {transformationCount, zeroCount};
    }
}
