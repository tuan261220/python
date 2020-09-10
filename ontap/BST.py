class Node:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    '''
        Cây nhị phân tìm kiếm.

        Các phần tử trên mỗi node là số nguyên
        Mỗi node là một đối tượng thuộc lớp Node dưới đây

        Mỗi node có 2 con là left và right, trong đó
        left < node < right


        Chú ý, với bài tập về cây, các phương thức thường được viết
        bằng các hàm đệ quy, sinh viên có thể viết thêm các hàm phụ trợ nếu cần
    '''

    def __init__(self):
        '''
        Các thao tác trên cây nhị phân sẽ được thực hiện thông qua tham chiếu tới
        nút gốc root
        '''
        self.root = None

    def getRoot(self):
        return self.root
    # Sinh viên hoàn thiện các hàm dưới đây
    # 2 hàm addNode và buildTreeFromList cần được hoàn thiện trước và chính xác,
    # nếu 2 hàm này chưa hoàn thiện
    # thì các hàm sau sẽ không được chấm điểm

    # Sinh viên cần hoàn thiện các hàm dưới đây

    # ===========================================================================================

    def addNode(self, data):
        '''
            Phương thức thêm 1 node với giá trị data (data là 1 số nguyên) vào cây
            nhị phân tìm kiếm
            Chú ý trường hợp khi thêm node đầu tiên vào cây, node này sẽ là node gốc root
            Hàm này bắt buộc phải làm đúng
        '''
        if(self.root == None) :
            self.root = Node(data)
        else:
            self._add(data,self.root)

    def _add(self,data,node):
        if(data < node.val) :
            if(node.left == None):
                node.left = Node(data)
            else:
                self._add(data,node.left)
        else:
            if(node.right == None):
                node.right = Node(data)
            else:
                self._add(data,node.right)

    def buildTreeFromList(self, datas):
        '''
            Phương thức dựng cây nhị phân tìm kiếm
            từ danh sách các phần tử datas (danh sách các số nguyên)
            phần tử đầu tiên trong danh sách là node gốc (root)
            Hàm này bắt buộc cần làm đúng
        '''
        for i in range(0,len(datas)) :
            self.addNode(datas[i])


    def search(self, val):
        '''
            Tìm kiếm xem giá trị val có trong cây hay không,
            Nếu có trả lại True, ngược lại trả lại False
        '''
        if(self.root != None ):
            return self._search(val,self.root)
        else:
            return None
    def _search(self,val,node):
        if(node.val == val):
            return True
        elif(val < node.val):
            if node.left == None:
                return False
            else:
                return self._search(val,node.left)
        elif(val > node.val):
            if node.right == None:
                return False
            else:
                return self._search(val,node.right)

    def preOrder(self):
        '''
            Hàm trả lại danh sách các giá trị trên các node trong cây theo thứ tự trước (tiền thứ tự)
            node -> left -> right
            Hàm này thường được viết dưới dạng đệ quy, nếu cần các bạn nên viết thêm các hàm phụ trợ
        '''
        self.list = []
        self._preOrder(self.root)
        return self.list
    def _preOrder(self,node):
        if(node != None):
            self.list.append(node.val)
            self._preOrder(node.left)
            self._preOrder(node.right)
    def inOrder(self):
        '''
            Hàm trả lại danh sách các giá trị trên các node trong cây theo thứ tự giữa (trung thứ tự)
            left -> node -> right
            Hàm này thường được viết dưới dạng đệ quy, nếu cần các bạn nên viết thêm các hàm phụ trợ
        '''
        self.list = []
        self._inOrder(self.root)
        return self.list
    def _inOrder(self,node):
        if(node != None):
            self._inOrder(node.left)
            self.list.append(node.val)
            self._inOrder(node.right)
    def postOrder(self):
        '''
            Hàm trả lại danh sách các giá trị trên các node trong cây theo thứ tự sau (hậu thứ tự)
           left -> right -> node

            Hàm này thường được viết dưới dạng đệ quy, nếu cần các bạn nên viết thêm các hàm phụ trợ
        '''
        self.list = []
        self._postOrder(self.root)
        return self.list
    def _postOrder(self,node):
        if(node != None):
            self._postOrder(node.left)
            self._postOrder(node.right)
            self.list.append(node.val)
    def getHeight(self):
        '''
            Hàm trả lại độ cao của cây,

            Độ cao của cây là số cạnh nhiều nhất trên các đường từ node gốc tới node lá

        '''
        return self.calHeight(self.root) - 1
    def calHeight(self,node):
        if (node == None):
            return 0
        else:
            return 1 + max(self.calHeight(node.left), self.calHeight(node.right))

    def getSumLeftChild(self, node):
        '''
            Hàm tính tổng các giá trị  trên cây con trái của node
        '''
        self.sum = 0
        self._getSumLeftChild(node.left)
        return self.sum
    def _getSumLeftChild(self,node):
        if node == None:
            self.sum += 0
        else:
            self.sum += int(node.val)
            self._getSumLeftChild(node.left)
            self._getSumLeftChild(node.right)
    def getSumRightChild(self, node):
        '''
            Hàm tính tổng các giá trị trên cây con phải của node
        '''
        self.sum = 0
        self._getSumRightChild(node.right)
        return self.sum

    def _getSumRightChild(self,node):
        if node == None:
            self.sum += 0
        else:
            self.sum += int(node.val)
            self._getSumRightChild(node.left)
            self._getSumRightChild(node.right)
    def getTilt(self):
        '''
            Hàm tính độ nghiêng của cây,

            Độ nghiêng của cây được tính bằng tổng độ nghiêng của các node trong cây

            Độ nghiêng của mỗi node được tính bằng
            giá trị tuyệt đối của (tổng các giá trị trên cây con trái trừ đi tổng các giá trị trên cây
            con phải của node đó)

        '''
        self.sum = 0
        self.calTilt(self.root)
        return self.sum
    def calTilt(self,node):
        if node != None :
            self.sum += abs(self.getSumLeftChild(node) - self.getSumRightChild(node))
            self.calTilt(node.right)
            self.calTilt(node.left)

    def printTree(self):
# Những dòng dưới đây là code chạy thử chương trình, sinh viên không cần chỉnh sửa

if __name__ == '__main__':
    bst = BinarySearchTree()

    datas = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]

    bst.buildTreeFromList(datas)
    print('Search 7:', bst.search(7))
    print('Search 12:', bst.search(12))

    print('PreOrder:', bst.preOrder())
    print('InOrder:', bst.inOrder())
    print('PostOrder:', bst.postOrder())
    print('Get height:', bst.getHeight())
    print('Sum of left child tree:', bst.getSumLeftChild(bst.getRoot()))
    print('Sum of right child tree:', bst.getSumRightChild(bst.getRoot()))
    print('Tilt of tree:', int(bst.getTilt()))