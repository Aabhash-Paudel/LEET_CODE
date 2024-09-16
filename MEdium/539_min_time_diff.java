class Solution {
    public int findMinDifference(List<String> timePoints) {
        if (timePoints.size() > 1440) {
            return 0; // If there are more than 1440 time points, there must be a duplicate
        }

        boolean[] minutesSeen = new boolean[1440]; // 24 * 60 = 1440 minutes in a day
        
        for (String time : timePoints) {
            int minutes = convertToMinutes(time);
            if (minutesSeen[minutes]) {
                return 0; // If we've seen this time before, the minimum difference is 0
            }
            minutesSeen[minutes] = true;
        }
        
        int firstMinute = -1;
        int prevMinute = -1;
        int minDiff = Integer.MAX_VALUE;
        
        for (int i = 0; i < 1440; i++) {
            if (minutesSeen[i]) {
                if (firstMinute == -1) {
                    firstMinute = i;
                    prevMinute = i;
                } else {
                    minDiff = Math.min(minDiff, i - prevMinute);
                    prevMinute = i;
                }
            }
        }
        
        // Check the difference between the last and first time (wrapping around midnight)
        minDiff = Math.min(minDiff, 1440 - prevMinute + firstMinute);
        
        return minDiff;
    }
    
    private int convertToMinutes(String time) {
        String[] parts = time.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        return hours * 60 + minutes;
    }
}