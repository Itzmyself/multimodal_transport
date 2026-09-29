SELECT *
FROM lines
WHERE highway IN (

'motorway',
'trunk',
'primary',
'secondary',
'tertiary',
'residential',
'unclassified',
'service',
'living_street'

)
