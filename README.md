# HOMEWORK_AI-Pacman_P1.Search
[19021635] - DƯƠNG THỊ TỐ UYÊN

Autograder: 

Question 1️⃣ ( depthFirstSearch )
    nodeStack - ngăn xếp dùng để chứa các node trong quá trình duyệt DFS.
    oldNode - 1 set lưu trữ các node đã duyệt qua
    currentNodeState - trạng thái, state của node hiện tại đang duyệt tới
    move - các bước đi (actions) từ vị trí ban đầu tới node hiện tại

    Duyệt DFS cho đến khi nodeStack không còn phần tử nào hoặc khi đạt được tới goalState

Question 2️⃣ ( breadthFirstSearch )
    Tương tự Question 1 nhưng thay vì sử dụng Stack thì ta sử dụng Queue để duyệt BFS

Question 3️⃣ ( uniformCostSearch )

👉 Thay vì sử dụng Queue thông thường, ta sử dụng PriorityQueue (hàng đợi ưu tiên) để duyệt UCS. Các node có mức độ ưu tiên cao hơn (chi phí thấp hơn) sẽ được duyệt trước.

👉 oldNode sử dụng kiểu dict thay vì set như các câu hỏi trước

👉 Trong quá trình duyệt các node, nếu phát hiện ra chi phí thấp hơn để tới currentNodeState thì tiến hành gán lại chi phí cho currentNodeState trong oldNode

👉 Duyệt UCS cho đến khi nodePriorityQueue không còn phần tử nào hoặc khi đạt được tới goalState

Question 4️⃣ ( A* search )

👉 Sử dụng Priority Queue tương tự Question 3.

👉 Thay đổi công thức tính độ ưu tiên của từng node trong Priority Queue theo công thức F = G + H

Question 5️⃣ ( CornersProblem )

👉 Tại hàm init ta lưu lại trạng thái bắt đầu của Pacman, có thể lấy bằng hàm getStartState(...). Kiểm tra Pacman khi bắt đầu đã nằm ở bất kỳ góc nào hay chưa.

👉 isGoalState(...) kiểm tra Pacman đã tới tất cả các góc hay chưa và trả về True/False

👉 getSuccessors(...) kiểm tra các hướng (xem có tường hay không), cập nhật trạng thái và trả về các successors có thể đi được.

👉 Sử dụng các thuật toán tìm kiếm đã làm ở các Question trên để giải quyết bài toán

Question 6️⃣ ( Corners Problem: Heuristic )

👉 Tạo thêm 2 hàm mới findClosestPoint và findFarthesetPoint trả về node gần nhất và xa nhất so với node hiện tại phục vụ cho việc tính toán ở Question #6 và #7

👉 Mảng unvisitedCorner chứa các góc chưa được đi tới

👉 Heuristic = currentToClosest + closestToFarthest

Question 7️⃣ ( Eating All The Dots )
 👉 Sử dụng findClosestPoint và findFarthesetPoint đã viết từ Question #6

👉 Thay vì một mảng chứa các góc chưa đi tới như #6, ở #7 ta dùng list foodList để lưu vị trí các food.

👉 Thuật toán tương tự với Question #6

Question 8️⃣ ( Suboptimal Search )

👉 Sử dụng thuật toán BreathFirstSearch để giải quyết bài toán

👉 isGoalState trả về trạng thái của vị trí hiện tại có phải là đích hay không
