docker cp ddl.cql cass-node:./ddl.cql


sec=3
while ! docker exec -it cass-node cqlsh -e "show host;" ; do
	echo "Enable to establish connection, will try again in $sec seconds."
	sleep $sec
	sec=$((sec+2))
done

docker exec -it cass-node cqlsh -f ./ddl.cql