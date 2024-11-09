zapros = '''SELECT 
    o.order_id AS Номер_заказа,
    o.period AS Дата_заказа,
    GROUP_CONCAT(b.product_name, ', ') AS Состав_заказа,
    SUM(b.price * ob.book_count) AS Сумма_заказа,
    SUM(b.price * ob.book_count * 0.1) AS Сумма_скидки, -- Предположим, скидка 10%
    pp.addres AS Пункт_выдачи
FROM 
    orders o
JOIN 
    order_books ob ON o.order_id = ob.order_id
JOIN 
    books b ON ob.book_id = b.product_id
JOIN 
    PickupPoints pp ON o.pp_id = pp.pp_id
GROUP BY 
    o.order_id, o.period, pp.addres;'''