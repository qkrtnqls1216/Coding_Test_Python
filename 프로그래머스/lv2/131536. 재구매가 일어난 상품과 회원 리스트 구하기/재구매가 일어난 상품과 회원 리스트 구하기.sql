select USER_ID,PRODUCT_ID
from ONLINE_SALE 
group by USER_ID,PRODUCT_ID
having count(*) > 1 # 1번이상 구매한 경우
order by USER_ID ASC, PRODUCT_ID DESC