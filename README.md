# HOMEWORK_AI-Pacman_P1.Search
[19021635] - DƯƠNG THỊ TỐ UYÊN

Autograder: 

![Screenshot 2022-04-21 142248](https://user-images.githubusercontent.com/93988845/164403532-1114cfca-30cf-45bf-badd-9d226f493238.png)


Question 1️⃣ ( depthFirstSearch ) 

    #nodeStack - ngăn xếp dùng để chứa các node trong quá trình duyệt DFS
    #visitedNodes - 1 set lưu trữ các node đã duyệt qua
    #currentNodeState - trạng thái (state) của node hiện tại đang duyệt
    #action - hành động, bước đi từ vị trí ban đầu tới node đang duyệt
    – Duyệt DFS cho đến khi nodeStack không còn phần tử nào hoặc khi đạt được tới goalState
![image](https://user-images.githubusercontent.com/93988845/164400279-f1ff381f-f998-40bd-b859-a310abeecd9b.png)


Question 2️⃣ ( breadthFirstSearch ) 

    - Tương tự Question 1 nhưng thay vì sử dụng Stack thì ta sử dụng Queue (hàng đợi) để duyệt BFS
![image](https://user-images.githubusercontent.com/93988845/164401130-6a4a632d-e530-46a6-81b0-f46110ac5270.png)


Question 3️⃣ ( uniformCostSearch )

    #cost - chi phí từ node đầu tiên tính đến node đang xét
    #visitedNode -  sử dụng kiểu {} dict thay vì Set() như 2 câu trước để lưu trữ các node đã duyệt kèm theo chi phí của chúng.
    
    - Sử dụng PriorityQueue (hàng đợi ưu tiên) thay vì Queue hay Stack để duyệt UCS
    Các node có chi phí (cost) thấp hơn sẽ được duyệt trước. 
    Trong quá trình duyệt các node, nếu phát hiện ra chi phí thấp hơn để tới currentNodeState 
    -> tiến hành gán lại chi phí cho currentNodeState trong visitedNode
![image](https://user-images.githubusercontent.com/93988845/164401641-482ef434-ebf9-4803-a994-e64ef024f0d6.png)


Question 4️⃣ ( A* search )

    #nodePriorityQueue - hàng đợi ưu tiên lưu trữ các node trong quá trình duyệt A*
    #visitedNodes - 1 set lưu trữ các node đã duyệt
    #cost - chi phí từ node đầu tiên tới node đang duyệt
    
    A* - kết hợp giữa BFS (g) và UCS (h): f = g + h
    UCS - chi phí từ node hiện tại đến node n (tối ưu nhưng chậm)
    BFS - ước lượng khoảng cách từ node n đến đích (nhanh nhưng k tối ưu)
![image](https://user-images.githubusercontent.com/93988845/164401892-a96f2e67-7489-419f-8629-a7eb5e2ed086.png)


Question 5️⃣ ( CornersProblem )

    - Tại hàm init ta lưu lại trạng thái bắt đầu của Pacman, có thể lấy bằng hàm getStartState(...). 
    Kiểm tra Pacman khi bắt đầu đã nằm ở bất kỳ góc nào hay chưa.
    - isGoalState(...) kiểm tra Pacman đã tới tất cả các góc hay chưa và trả về True/False
    - getSuccessors(...) kiểm tra các hướng (xem có tường hay không), cập nhật trạng thái và trả về các successors có thể đi được.
    - Sử dụng các thuật toán tìm kiếm đã làm ở các Question trên để giải quyết bài toán
![image](https://user-images.githubusercontent.com/93988845/164402402-0e11d640-3980-4ee1-a7c8-5404b8167349.png)
![image](https://user-images.githubusercontent.com/93988845/164402611-c5996206-a5b4-46aa-ba7e-9046ad67a6ac.png)
![image](https://user-images.githubusercontent.com/93988845/164402744-cad94f62-2547-4354-94c1-c17c9d0a1e47.png)


Question 6️⃣ ( Corners Problem: Heuristic )

    - Tạo thêm 2 hàm mới findClosestPoint và findFarthesetPoint trả về node gần nhất và xa nhất so với node hiện tại 
    (phục vụ cho việc tính toán ở cả câu 6 và câu 7)
    - Mảng unvisitedCorner chứa các góc chưa được đi tới
    - Heuristic = currentToClosest + closestToFarthest
![image](https://user-images.githubusercontent.com/93988845/164402915-634c4daf-0982-4b89-bea0-80ecf0841ee2.png)
![image](https://user-images.githubusercontent.com/93988845/164402983-0b1cccf1-fdc7-480c-aea1-7c7535ee2ae5.png)


Question 7️⃣ ( Eating All The Dots )

    - Sử dụng findClosestPoint và findFarthesetPoint đã viết từ Question #6
    - Thay vì một mảng chứa các góc chưa đi tới như #6, ở #7 ta dùng list foodList để lưu vị trí các food.
    - Thuật toán tương tự với Question #6
![image](https://user-images.githubusercontent.com/93988845/164403082-e0a4f2d2-a524-4dd9-a262-3d67c8596357.png)


Question 8️⃣ ( Suboptimal Search )

    - Sử dụng thuật toán BreathFirstSearch để giải quyết bài toán
    - isGoalState trả về trạng thái của vị trí hiện tại có phải là đích hay không
![image](https://user-images.githubusercontent.com/93988845/164403177-fa83b2cf-5aca-43e4-95d4-69097b572bdc.png)
![image](https://user-images.githubusercontent.com/93988845/164403230-9e875041-71b1-4056-ae41-d08b98b94af4.png)
