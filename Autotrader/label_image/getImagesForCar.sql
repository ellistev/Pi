select top 1 adid, make, model, categorypath from adsell where make = 'volkswagen' and model = 'golf'


select top 1000 imagepath from adphoto (nolock) where adid in 
(select adid  from ad where Ad.AdAttributes.value('(//attributes/attribute[@id="128"]/item/@value)[1]','nvarchar(100)')  = '2/7/2000378/2044399') 
and ismainphoto = 1

