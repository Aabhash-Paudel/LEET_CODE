import java.util.*;

/**
 * 1331_rank_trans_arr
 */
public class test {
    public int[] arrayRankTransform(int[] arr) {
        Map<Integer, Integer> dict = new HashMap<>();
        int[] srtd = Arrays.stream(arr).distinct().sorted().toArray();

        for (int i = 0; i < srtd.length; i++) {
            dict.put(srtd[i], i + 1);
        }
        
        // Replace each element in the original array with its rank
        for (int i = 0; i < arr.length; i++) {
            arr[i] = dict.get(arr[i]);
        }
        
        return arr;

    }
    public static void main(String[] args) {
        test t = new test();
        int[] arr = {100, 100, 100,200,300};
        int[] result = t.arrayRankTransform(arr);
        System.out.println("Original array: " + Arrays.toString(arr));
        System.out.println("Transformed array (rank): " + Arrays.toString(result));
    }

}