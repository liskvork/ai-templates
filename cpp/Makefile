# Sample Makefile, it is not good

NAME	=	pbrain-cpp-template

CXXFLAGS	=	-Wall -Wextra -Wconversion

all: $(NAME)

$(NAME): main.o
	$(CXX) main.o -o $(NAME)

clean:
	rm -f main.o

fclean: clean
	rm -f $(NAME)

re: fclean
	$(MAKE) all
