/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    const nearest = []
    let longestDistance = [0, -1]
    
    for(let i = 0; i < k; i++) {
        for(let j = i; j < points.length; j++){
            const [x, y] = points[i]
            const distance = x ** 2 + y ** 2  
            const [x1, y1] = points[j]
            const distance2 = x1 ** 2 + y1 ** 2
            if(distance > distance2){
                [points[i], points[j]] = [points[j], points[i]]
            }
        }   
    }
    
    return points.slice(0, k)
};