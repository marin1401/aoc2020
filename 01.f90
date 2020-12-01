program day01
  
  integer input(200)
  integer sum,mul
  
  !Read input
  
  open(10, file="01.txt")
  
  do i = 1,size(input)
    read(10,*) input(i)
  end do
  
  !Part 1
  
  outer: do i = 1,size(input)
    do j = 1,size(input)
      sum = input(i)+input(j)
      if(sum.eq.2020) then
        mul = input(i)*input(j)
        print *,mul
        exit outer
      end if
    end do
  end do outer
  
  !Part 2
  
  do i = 1,size(input)
    do j = 1,size(input)
      do k = 1,size(input)
        sum = input(i)+input(j)+input(k)
        if(sum.eq.2020) then
          mul = input(i)*input(j)*input(k)
          print *,mul
          stop
        end if
      end do
    end do
  end do
  
end program day01