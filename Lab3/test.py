from crr_model import *
def main():
    binomial_tree = Node.build_recombining_tree(4)
    print(binomial_tree.left.left.right.val)
    binomial_tree.left.right.left.val = 2
    print(binomial_tree.left.left.right.val)

if __name__ == "__main__":
    main()
