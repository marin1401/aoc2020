program day01
  
  integer input(200)
  integer dim,sum,mul
  
  !Read input
  
  open(10, file="01.txt")
  
  dim = size(input)
  
  do i = 1,dim
    read(10,*) input(i)
  end do
  
  !Part 1
  
  outer: do i = 1,dim
    do j = 1,dim
      sum = input(i) + input(j)
      if(sum.eq.2020) then
        mul = input(i) * input(j)
        print *, mul
        exit outer
      end if
    end do
  end do outer
  
  !Part 2
  
  do i = 1,dim
    do j = 1,dim
      do k = 1,dim
        sum = input(i) + input(j) + input(k)
        if(sum.eq.2020) then
          mul = input(i) * input(j) * input(k)
          print *, mul
          stop
        end if
      end do
    end do
  end do
  
end program day01
