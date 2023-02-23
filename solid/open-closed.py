from abc import ABC, abstractmethod


class Operations(ABC):
    @abstractmethod
    def operation():
        pass


class Min(Operations):
    def operation(nums):
        print(f"The min is {min(nums)}")


class Max(Operations):
    def operation(nums):
        print(f"The max is {max(nums)}")


class Main:
    @abstractmethod
    def get_operations(nums):
        # __subclasses__ will found all classes inheriting from Operations
        for operation in Operations.__subclasses__():
            operation.operation(nums)


if __name__ == "__main__":
    Main.get_operations(range(10))
