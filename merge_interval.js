/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
    // [[2,3],[4,6],[5,7],[3,4]]
    const merged = []
    const mergedIndices = new Map()

    for(let i = 0; i < intervals.length; i++){
        if(mergedIndices.has(i)) continue;

        for(let j = i + 1; j < intervals.length; j++){
            if(mergedIndices.has(j)) continue;

            const [x1, x2] = intervals[i]
            const [y1, y2] = intervals[j]
      
            if ((y1 <= x2 && x1 <= y2) || (x1 <= y2 && y1 < x2)) {
              mergedIndices.set(j, true)

              intervals[i][0] = x1 < y1 ? x1 : y1
              intervals[i][1] = x2 < y2 ? y2 : x2

              j = i
            }

        }
        merged.push(intervals[i])
    }
    return merged
}