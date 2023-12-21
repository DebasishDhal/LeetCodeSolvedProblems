/*
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Constraints:

n == points.length
2 <= n <= 105
points[i].length == 2
0 <= xi, yi <= 109
*/
//My solution, beats 5% only.
var maxWidthOfVerticalArea = function(points){
  points.sort((a,b)=>(a[0]-b[0]))

  let maxArea = 0
  for (let pos = 0; pos<points.length-1; pos++){
    let area = points[pos+1][0]-points[pos][0]
    maxArea = Math.max(area,maxArea) //Replace this line with if (area > maxArea) maxArea = area; The performance shoots up to 80%
  }

  return maxArea
}
