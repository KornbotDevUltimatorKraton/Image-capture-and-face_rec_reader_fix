cam_num= 1
#print("for r_"+str(cam_num)+" in count(0):"+"\n\t\tpacket_"+str(cam_num)+",_"+str(cam_num)+" = client_socket_"+str(cam_num)+".recvfrom(BUFF_SIZE_"+str(cam_num)+")"+"\n\t\tdata_"+str(cam_num)+" = base64.b64decode(packet_"+str(cam_num)+",' /')"+"\n\t\tnpdata_"+str(cam_num)+" = np.fromstring(data_"+str(cam_num)+",dtype=np.uint8)"+"\n\t\tframe_"+str(cam_num)+" = cv2.imdecode(npdata_"+str(cam_num)+",1)"+"\n\t\tprint(frame_"+str(cam_num)+")"+"\n\t\tsmall_frame_"+str(cam_num)+" = cv2.resize(frame_"+str(cam_num)+", (0, 0), fx=0.25, fy=0.25)"+"\n\t\trgb_small_frame_"+str(cam_num)+" = small_frame_"+str(cam_num)+"[:, :, ::-1]"+"\n\t\tif process_this_frame:"+"\n\t\t\tface_locations_"+str(cam_num)+" = face_recognition.face_locations(rgb_small_frame_"+str(cam_num)+")"+"\n\t\t\tface_encodings_"+str(cam_num)+" = face_recognition.face_encodings(rgb_small_frame_"+str(cam_num)+", face_locations_"+str(cam_num)+")"+"\n\t\t\tface_names = []"+"\n\t\t\tfor face_encoding in face_encodings"+str(cam_num)+":"+"\n\t\t\t\tmatches_"+str(cam_num)+" = face_recognition.compare(known_face_encodings, face_encoding)"+"\n\t\t\t\tname = 'Unknown'"+"\n\t\t\t\tface_distances_"+str(cam_num)+" = face_recognition.face_distance(known_face_encodings, face_encoding)"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tif matches_"+str(cam_num)+"[best_match_index"+str(cam_num)+"]:"+"\n\t\t\t\t\tname = known_face_names[best_match_index_"+str(cam_num)+"]"+"\n\t\t\t\tface_names.append(name)"+"\n\t\t\t\tprint(frame)")
#print("for r_"+str(cam_num)+" in count(0):"+"\n\t\tpacket_"+str(cam_num)+",_"+str(cam_num)+" = client_socket_"+str(cam_num)+".recvfrom(BUFF_SIZE_"+str(cam_num)+")"+"\n\t\tdata_"+str(cam_num)+" = base64.b64decode(packet_"+str(cam_num)+",' /')"+"\n\t\tnpdata_"+str(cam_num)+" = np.fromstring(data_"+str(cam_num)+",dtype=np.uint8)"+"\n\t\tframe_"+str(cam_num)+" = cv2.imdecode(npdata_"+str(cam_num)+",1)"+"\n\t\tprint(frame_"+str(cam_num)+")"+"\n\t\tsmall_frame_"+str(cam_num)+" = cv2.resize(frame_"+str(cam_num)+", (0, 0), fx=0.25, fy=0.25)"+"\n\t\trgb_small_frame_"+str(cam_num)+" = small_frame_"+str(cam_num)+"[:, :, ::-1]"+"\n\t\tif process_this_frame:"+"\n\t\t\tface_locations_"+str(cam_num)+" = face_recognition.face_locations(rgb_small_frame_"+str(cam_num)+")"+"\n\t\t\tface_encodings_"+str(cam_num)+" = face_recognition.face_encodings(rgb_small_frame_"+str(cam_num)+", face_locations_"+str(cam_num)+")"+"\n\t\t\tface_names = []"+"\n\t\t\tfor face_encoding in face_encodings"+str(cam_num)+":"+"\n\t\t\t\tmatches_"+str(cam_num)+" = face_recognition.compare(known_face_encodings, face_encoding)"+"\n\t\t\t\tname = 'Unknown')"+"\n\t\t\t\tface_distances_"+str(cam_num)+" = face_recognition.face_distance(known_face_encodings, face_encoding)"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tif matches_"+str(cam_num)+"[best_match_index"+str(cam_num)+"]:"+"\n\t\t\t\t\tname = known_face_names[best_match_index_"+str(cam_num)+"]"+"\n\t\t\t\tface_names.append(name)"+"\n\t\t\t\tprint(frame)"+"\n\t\tprocess_this_frame = not process_this_frame")
#print("for r_"+str(cam_num)+" in count(0):"+"\n\t\tpacket_"+str(cam_num)+",_"+str(cam_num)+" = client_socket_"+str(cam_num)+".recvfrom(BUFF_SIZE_"+str(cam_num)+")"+"\n\t\tdata_"+str(cam_num)+" = base64.b64decode(packet_"+str(cam_num)+",' /')"+"\n\t\tnpdata_"+str(cam_num)+" = np.fromstring(data_"+str(cam_num)+",dtype=np.uint8)"+"\n\t\tframe_"+str(cam_num)+" = cv2.imdecode(npdata_"+str(cam_num)+",1)"+"\n\t\tprint(frame_"+str(cam_num)+")"+"\n\t\tsmall_frame_"+str(cam_num)+" = cv2.resize(frame_"+str(cam_num)+", (0, 0), fx=0.25, fy=0.25)"+"\n\t\trgb_small_frame_"+str(cam_num)+" = small_frame_"+str(cam_num)+"[:, :, ::-1]"+"\n\t\tif process_this_frame:"+"\n\t\t\tface_locations_"+str(cam_num)+" = face_recognition.face_locations(rgb_small_frame_"+str(cam_num)+")"+"\n\t\t\tface_encodings_"+str(cam_num)+" = face_recognition.face_encodings(rgb_small_frame_"+str(cam_num)+", face_locations_"+str(cam_num)+")"+"\n\t\t\tface_names = []"+"\n\t\t\tfor face_encoding in face_encodings"+str(cam_num)+":"+"\n\t\t\t\tmatches_"+str(cam_num)+" = face_recognition.compare(known_face_encodings, face_encoding)"+"\n\t\t\t\tname = 'Unknown')"+"\n\t\t\t\tface_distances_"+str(cam_num)+" = face_recognition.face_distance(known_face_encodings, face_encoding)"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tif matches_"+str(cam_num)+"[best_match_index"+str(cam_num)+"]:"+"\n\t\t\t\t\tname = known_face_names[best_match_index_"+str(cam_num)+"]"+"\n\t\t\t\tface_names.append(name)"+"\n\t\t\t\tprint(frame)"+"\n\t\tprocess_this_frame = not process_this_frame"+"\n\t\tfor (top, right, bottom, left), name in zip(face_locations, face_names):"+"\n\t\t\ttop *=4"+"\n\t\t\tright *=4"+"\n\t\t\tbottom *=4"+"\n\t\t\tleft *=4"+"\n\t\t\tcv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)"+"\n\t\t\tcv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)"+"\n\t\t\tfont = cv2.FONT_HERSHEY_DUPLEX"+"\n\t\t\tcv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)"+"\n\t\tcv2.imshow('Face_recognition', frame)"+"\n\t\tif cv2.waitKey(1) & 0xFF == ord('q'):"+"\n\t\t\tbreak")
print("for r_"+str(cam_num)+" in count(0):"+"\n\t\tpacket_"+str(cam_num)+",_"+str(cam_num)+" = client_socket_"+str(cam_num)+".recvfrom(BUFF_SIZE_"+str(cam_num)+")"+"\n\t\tdata_"+str(cam_num)+" = base64.b64decode(packet_"+str(cam_num)+",' /')"+"\n\t\tnpdata_"+str(cam_num)+" = np.fromstring(data_"+str(cam_num)+",dtype=np.uint8)"+"\n\t\tframe_"+str(cam_num)+" = cv2.imdecode(npdata_"+str(cam_num)+",1)"+"\n\t\tprint(frame_"+str(cam_num)+")"+"\n\t\tsmall_frame_"+str(cam_num)+" = cv2.resize(frame_"+str(cam_num)+", (0, 0), fx=0.25, fy=0.25)"+"\n\t\trgb_small_frame_"+str(cam_num)+" = small_frame_"+str(cam_num)+"[:, :, ::-1]"+"\n\t\tif process_this_frame:"+"\n\t\t\tface_locations_"+str(cam_num)+" = face_recognition.face_locations(rgb_small_frame_"+str(cam_num)+")"+"\n\t\t\tface_encodings_"+str(cam_num)+" = face_recognition.face_encodings(rgb_small_frame_"+str(cam_num)+", face_locations_"+str(cam_num)+")"+"\n\t\t\tface_names = []"+"\n\t\t\tfor face_encoding in face_encodings_"+str(cam_num)+":"+"\n\t\t\t\tmatches_"+str(cam_num)+" = face_recognition.compare(known_face_encodings, face_encoding)"+"\n\t\t\t\tname = 'Unknown'"+"\n\t\t\t\tface_distances_"+str(cam_num)+" = face_recognition.face_distance(known_face_encodings, face_encoding)"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tbest_match_index = np.argmin(face_distances_"+str(cam_num)+")"+"\n\t\t\t\tif matches_"+str(cam_num)+"[best_match_index"+str(cam_num)+"]:"+"\n\t\t\t\t\tname = known_face_names[best_match_index_"+str(cam_num)+"]"+"\n\t\t\t\tface_names.append(name)"+"\n\t\t\t\tprint(frame_"+str(cam_num)+")"+"\n\t\tprocess_this_frame = not process_this_frame"+"\n\t\tfor (top, right, bottom, left), name in zip(face_locations"+str(cam_num)+", face_names):"+"\n\t\t\ttop *=4"+"\n\t\t\tright *=4"+"\n\t\t\tbottom *=4"+"\n\t\t\tleft *=4"+"\n\t\t\tcv2.rectangle(frame_"+str(cam_num)+", (left, top), (right, bottom), (0, 0, 255), 2)"+"\n\t\t\tcv2.rectangle(frame_"+str(cam_num)+", (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)"+"\n\t\t\tfont = cv2.FONT_HERSHEY_DUPLEX"+"\n\t\t\tcv2.putText(frame_"+str(cam_num)+", name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)"+"\n\t\tcv2.imshow('Face_recognition', frame_"+str(cam_num)+")"+"\n\t\tif cv2.waitKey(1) & 0xFF == ord('q'):"+"\n\t\t\tbreak")