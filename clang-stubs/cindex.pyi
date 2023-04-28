from ctypes import Structure, pointer, c_void_p, CDLL
import typing

_T = typing.TypeVar('_T')
_CObjectPtr = typing.Type[pointer[c_void_p]]


class TranslationUnitLoadError(Exception):
    pass


class TranslationUnitSaveError(Exception):
    ERROR_UNKNOWN: int
    ERROR_TRANSLATION_ERRORS: int
    ERROR_INVALID_TU: int

    def __init__(self, enumeration: int, message: str) -> None: ...


class SourceLocation(Structure):
    @staticmethod
    def from_position(tu: 'TranslationUnit', file: str, line: int, column: int) -> 'SourceLocation': ...
    @staticmethod
    def from_offset(tu: 'TranslationUnit', file: str, offset: int) -> 'SourceLocation': ...
    @property
    def file(self) -> typing.Optional['File']: ...
    @property
    def line(self) -> int: ...
    @property
    def column(self) -> int: ...
    @property
    def offset(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...


class SourceRange(Structure):
    @staticmethod
    def from_locations(start: int, end: int) -> 'SourceRange': ...
    @property
    def start(self) -> 'SourceLocation': ...
    @property
    def end(self) -> 'SourceLocation': ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __contains__(self, other: 'SourceLocation') -> bool: ...
    def __repr__(self) -> str: ...


class Diagnostic():
    Ignored: int
    Note: int
    Warning: int
    Error: int
    Fatal: int

    DisplaySourceLocation: int
    DisplayColumn: int
    DisplaySourceRanges: int
    DisplayOption: int
    DisplayCategoryId: int
    DisplayCategoryName: int

    def __del__(self) -> None: ...
    @property
    def severity(self) -> int: ...
    @property
    def location(self) -> 'SourceLocation': ...
    @property
    def spelling(self) -> str: ...
    @property
    def ranges(self) -> typing.Iterator['SourceRange']: ...
    @property
    def fixits(self) -> typing.Iterator['FixIt']: ...
    @property
    def children(self) -> typing.Iterator['Diagnostic']: ...
    @property
    def category_number(self) -> int: ...
    @property
    def category_name(self) -> str: ...
    @property
    def option(self) -> str: ...
    @property
    def disable_option(self) -> str: ...
    def format(self, options: typing.Optional[int] = ...) -> str: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class FixIt():
    def __init__(self, range: 'SourceRange', value: str) -> None: ...
    def __repr__(self) -> str: ...
    range: 'SourceRange'
    value: str


class TokenKind():
    def __init__(self, value: int, name: str) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def from_value(value: int) -> 'TokenKind': ...
    @staticmethod
    def register(value: int, name: str) -> None: ...

    PUNCTUATION: 'TokenKind'
    KEYWORD: 'TokenKind'
    IDENTIFIER: 'TokenKind'
    LITERAL: 'TokenKind'
    COMMENT: 'TokenKind'
    

class BaseEnumeration():
    def __init__(self, value: int) -> None: ...

    def from_param(self): int

    @property
    def name(self): str

    @classmethod
    def from_id(cls: type[_T], id: int) -> _T: ...

    def __repr__(self) -> str: ...


class CursorKind(BaseEnumeration):
    @staticmethod
    def get_all_kinds() -> typing.List['CursorKind']: ...


    def is_attribute(self) -> bool: ...
    def is_declaration(self) -> bool: ...
    def is_expression(self) -> bool: ...
    def is_invalid(self) -> bool: ...
    def is_preprocessing(self) -> bool: ...
    def is_reference(self) -> bool: ...
    def is_statement(self) -> bool: ...
    def is_translation_unit(self) -> bool: ...
    def is_unexposed(self) -> bool: ...
    
    UNEXPOSED_DECL: 'CursorKind'
    STRUCT_DECL: 'CursorKind'
    UNION_DECL: 'CursorKind'
    CLASS_DECL: 'CursorKind'
    ENUM_DECL: 'CursorKind'
    FIELD_DECL: 'CursorKind'
    ENUM_CONSTANT_DECL: 'CursorKind'
    FUNCTION_DECL: 'CursorKind'
    VAR_DECL: 'CursorKind'
    PARM_DECL: 'CursorKind'
    OBJC_INTERFACE_DECL: 'CursorKind'
    OBJC_CATEGORY_DECL: 'CursorKind'
    OBJC_PROTOCOL_DECL: 'CursorKind'
    OBJC_PROPERTY_DECL: 'CursorKind'
    OBJC_IVAR_DECL: 'CursorKind'
    OBJC_INSTANCE_METHOD_DECL: 'CursorKind'
    OBJC_CLASS_METHOD_DECL: 'CursorKind'
    OBJC_IMPLEMENTATION_DECL: 'CursorKind'
    OBJC_CATEGORY_IMPL_DECL: 'CursorKind'
    TYPEDEF_DECL: 'CursorKind'
    CXX_METHOD: 'CursorKind'
    NAMESPACE: 'CursorKind'
    LINKAGE_SPEC: 'CursorKind'
    CONSTRUCTOR: 'CursorKind'
    DESTRUCTOR: 'CursorKind'
    CONVERSION_FUNCTION: 'CursorKind'
    TEMPLATE_TYPE_PARAMETER: 'CursorKind'
    TEMPLATE_NON_TYPE_PARAMETER: 'CursorKind'
    TEMPLATE_TEMPLATE_PARAMETER: 'CursorKind'
    FUNCTION_TEMPLATE: 'CursorKind'
    CLASS_TEMPLATE: 'CursorKind'
    CLASS_TEMPLATE_PARTIAL_SPECIALIZATION: 'CursorKind'
    NAMESPACE_ALIAS: 'CursorKind'
    USING_DIRECTIVE: 'CursorKind'
    USING_DECLARATION: 'CursorKind'
    TYPE_ALIAS_DECL: 'CursorKind'
    OBJC_SYNTHESIZE_DECL: 'CursorKind'
    OBJC_DYNAMIC_DECL: 'CursorKind'
    CXX_ACCESS_SPEC_DECL: 'CursorKind'
    OBJC_SUPER_CLASS_REF: 'CursorKind'
    OBJC_PROTOCOL_REF: 'CursorKind'
    OBJC_CLASS_REF: 'CursorKind'
    TYPE_REF: 'CursorKind'
    CXX_BASE_SPECIFIER: 'CursorKind'
    TEMPLATE_REF: 'CursorKind'
    NAMESPACE_REF: 'CursorKind'
    MEMBER_REF: 'CursorKind'
    LABEL_REF: 'CursorKind'
    OVERLOADED_DECL_REF: 'CursorKind'
    VARIABLE_REF: 'CursorKind'
    INVALID_FILE: 'CursorKind'
    NO_DECL_FOUND: 'CursorKind'
    NOT_IMPLEMENTED: 'CursorKind'
    INVALID_CODE: 'CursorKind'
    UNEXPOSED_EXPR: 'CursorKind'
    DECL_REF_EXPR: 'CursorKind'
    MEMBER_REF_EXPR: 'CursorKind'
    CALL_EXPR: 'CursorKind'
    OBJC_MESSAGE_EXPR: 'CursorKind'
    BLOCK_EXPR: 'CursorKind'
    INTEGER_LITERAL: 'CursorKind'
    FLOATING_LITERAL: 'CursorKind'
    IMAGINARY_LITERAL: 'CursorKind'
    STRING_LITERAL: 'CursorKind'
    CHARACTER_LITERAL: 'CursorKind'
    PAREN_EXPR: 'CursorKind'
    UNARY_OPERATOR: 'CursorKind'
    ARRAY_SUBSCRIPT_EXPR: 'CursorKind'
    BINARY_OPERATOR: 'CursorKind'
    COMPOUND_ASSIGNMENT_OPERATOR: 'CursorKind'
    CONDITIONAL_OPERATOR: 'CursorKind'
    CSTYLE_CAST_EXPR: 'CursorKind'
    COMPOUND_LITERAL_EXPR: 'CursorKind'
    INIT_LIST_EXPR: 'CursorKind'
    ADDR_LABEL_EXPR: 'CursorKind'
    StmtExpr: 'CursorKind'
    GENERIC_SELECTION_EXPR: 'CursorKind'
    GNU_NULL_EXPR: 'CursorKind'
    CXX_STATIC_CAST_EXPR: 'CursorKind'
    CXX_DYNAMIC_CAST_EXPR: 'CursorKind'
    CXX_REINTERPRET_CAST_EXPR: 'CursorKind'
    CXX_CONST_CAST_EXPR: 'CursorKind'
    CXX_FUNCTIONAL_CAST_EXPR: 'CursorKind'
    CXX_TYPEID_EXPR: 'CursorKind'
    CXX_BOOL_LITERAL_EXPR: 'CursorKind'
    CXX_NULL_PTR_LITERAL_EXPR: 'CursorKind'
    CXX_THIS_EXPR: 'CursorKind'
    CXX_THROW_EXPR: 'CursorKind'
    CXX_NEW_EXPR: 'CursorKind'
    CXX_DELETE_EXPR: 'CursorKind'
    CXX_UNARY_EXPR: 'CursorKind'
    OBJC_STRING_LITERAL: 'CursorKind'
    OBJC_ENCODE_EXPR: 'CursorKind'
    OBJC_SELECTOR_EXPR: 'CursorKind'
    OBJC_PROTOCOL_EXPR: 'CursorKind'
    OBJC_BRIDGE_CAST_EXPR: 'CursorKind'
    PACK_EXPANSION_EXPR: 'CursorKind'
    SIZE_OF_PACK_EXPR: 'CursorKind'
    LAMBDA_EXPR: 'CursorKind'
    OBJ_BOOL_LITERAL_EXPR: 'CursorKind'
    OBJ_SELF_EXPR: 'CursorKind'
    OMP_ARRAY_SECTION_EXPR: 'CursorKind'
    OBJC_AVAILABILITY_CHECK_EXPR: 'CursorKind'
    UNEXPOSED_STMT: 'CursorKind'
    LABEL_STMT: 'CursorKind'
    COMPOUND_STMT: 'CursorKind'
    CASE_STMT: 'CursorKind'
    DEFAULT_STMT: 'CursorKind'
    IF_STMT: 'CursorKind'
    SWITCH_STMT: 'CursorKind'
    WHILE_STMT: 'CursorKind'
    DO_STMT: 'CursorKind'
    FOR_STMT: 'CursorKind'
    GOTO_STMT: 'CursorKind'
    INDIRECT_GOTO_STMT: 'CursorKind'
    CONTINUE_STMT: 'CursorKind'
    BREAK_STMT: 'CursorKind'
    RETURN_STMT: 'CursorKind'
    ASM_STMT: 'CursorKind'
    OBJC_AT_TRY_STMT: 'CursorKind'
    OBJC_AT_CATCH_STMT: 'CursorKind'
    OBJC_AT_FINALLY_STMT: 'CursorKind'
    OBJC_AT_THROW_STMT: 'CursorKind'
    OBJC_AT_SYNCHRONIZED_STMT: 'CursorKind'
    OBJC_AUTORELEASE_POOL_STMT: 'CursorKind'
    OBJC_FOR_COLLECTION_STMT: 'CursorKind'
    CXX_CATCH_STMT: 'CursorKind'
    CXX_TRY_STMT: 'CursorKind'
    CXX_FOR_RANGE_STMT: 'CursorKind'
    SEH_TRY_STMT: 'CursorKind'
    SEH_EXCEPT_STMT: 'CursorKind'
    SEH_FINALLY_STMT: 'CursorKind'
    MS_ASM_STMT: 'CursorKind'
    NULL_STMT: 'CursorKind'
    DECL_STMT: 'CursorKind'
    OMP_PARALLEL_DIRECTIVE: 'CursorKind'
    OMP_SIMD_DIRECTIVE: 'CursorKind'
    OMP_FOR_DIRECTIVE: 'CursorKind'
    OMP_SECTIONS_DIRECTIVE: 'CursorKind'
    OMP_SECTION_DIRECTIVE: 'CursorKind'
    OMP_SINGLE_DIRECTIVE: 'CursorKind'
    OMP_PARALLEL_FOR_DIRECTIVE: 'CursorKind'
    OMP_PARALLEL_SECTIONS_DIRECTIVE: 'CursorKind'
    OMP_TASK_DIRECTIVE: 'CursorKind'
    OMP_MASTER_DIRECTIVE: 'CursorKind'
    OMP_CRITICAL_DIRECTIVE: 'CursorKind'
    OMP_TASKYIELD_DIRECTIVE: 'CursorKind'
    OMP_BARRIER_DIRECTIVE: 'CursorKind'
    OMP_TASKWAIT_DIRECTIVE: 'CursorKind'
    OMP_FLUSH_DIRECTIVE: 'CursorKind'
    SEH_LEAVE_STMT: 'CursorKind'
    OMP_ORDERED_DIRECTIVE: 'CursorKind'
    OMP_ATOMIC_DIRECTIVE: 'CursorKind'
    OMP_FOR_SIMD_DIRECTIVE: 'CursorKind'
    OMP_PARALLELFORSIMD_DIRECTIVE: 'CursorKind'
    OMP_TARGET_DIRECTIVE: 'CursorKind'
    OMP_TEAMS_DIRECTIVE: 'CursorKind'
    OMP_TASKGROUP_DIRECTIVE: 'CursorKind'
    OMP_CANCELLATION_POINT_DIRECTIVE: 'CursorKind'
    OMP_CANCEL_DIRECTIVE: 'CursorKind'
    OMP_TARGET_DATA_DIRECTIVE: 'CursorKind'
    OMP_TASK_LOOP_DIRECTIVE: 'CursorKind'
    OMP_TASK_LOOP_SIMD_DIRECTIVE: 'CursorKind'
    OMP_DISTRIBUTE_DIRECTIVE: 'CursorKind'
    OMP_TARGET_ENTER_DATA_DIRECTIVE: 'CursorKind'
    OMP_TARGET_EXIT_DATA_DIRECTIVE: 'CursorKind'
    OMP_TARGET_PARALLEL_DIRECTIVE: 'CursorKind'
    OMP_TARGET_PARALLELFOR_DIRECTIVE: 'CursorKind'
    OMP_TARGET_UPDATE_DIRECTIVE: 'CursorKind'
    OMP_DISTRIBUTE_PARALLELFOR_DIRECTIVE: 'CursorKind'
    OMP_DISTRIBUTE_PARALLEL_FOR_SIMD_DIRECTIVE: 'CursorKind'
    OMP_DISTRIBUTE_SIMD_DIRECTIVE: 'CursorKind'
    OMP_TARGET_PARALLEL_FOR_SIMD_DIRECTIVE: 'CursorKind'
    OMP_TARGET_SIMD_DIRECTIVE: 'CursorKind'
    OMP_TEAMS_DISTRIBUTE_DIRECTIVE: 'CursorKind'
    TRANSLATION_UNIT: 'CursorKind'
    UNEXPOSED_ATTR: 'CursorKind'
    IB_ACTION_ATTR: 'CursorKind'
    IB_OUTLET_ATTR: 'CursorKind'
    IB_OUTLET_COLLECTION_ATTR: 'CursorKind'
    CXX_FINAL_ATTR: 'CursorKind'
    CXX_OVERRIDE_ATTR: 'CursorKind'
    ANNOTATE_ATTR: 'CursorKind'
    ASM_LABEL_ATTR: 'CursorKind'
    PACKED_ATTR: 'CursorKind'
    PURE_ATTR: 'CursorKind'
    CONST_ATTR: 'CursorKind'
    NODUPLICATE_ATTR: 'CursorKind'
    CUDACONSTANT_ATTR: 'CursorKind'
    CUDADEVICE_ATTR: 'CursorKind'
    CUDAGLOBAL_ATTR: 'CursorKind'
    CUDAHOST_ATTR: 'CursorKind'
    CUDASHARED_ATTR: 'CursorKind'
    VISIBILITY_ATTR: 'CursorKind'
    DLLEXPORT_ATTR: 'CursorKind'
    DLLIMPORT_ATTR: 'CursorKind'
    CONVERGENT_ATTR: 'CursorKind'
    WARN_UNUSED_ATTR: 'CursorKind'
    WARN_UNUSED_RESULT_ATTR: 'CursorKind'
    ALIGNED_ATTR: 'CursorKind'
    PREPROCESSING_DIRECTIVE: 'CursorKind'
    MACRO_DEFINITION: 'CursorKind'
    MACRO_INSTANTIATION: 'CursorKind'
    INCLUSION_DIRECTIVE: 'CursorKind'
    MODULE_IMPORT_DECL: 'CursorKind'
    TYPE_ALIAS_TEMPLATE_DECL: 'CursorKind'
    STATIC_ASSERT: 'CursorKind'
    FRIEND_DECL: 'CursorKind'
    OVERLOAD_CANDIDATE: 'CursorKind'
    

class TemplateArgumentKind(BaseEnumeration):
    NULL: 'TemplateArgumentKind'
    TYPE: 'TemplateArgumentKind'
    DECLARATION: 'TemplateArgumentKind'
    NULLPTR: 'TemplateArgumentKind'
    INTEGRAL: 'TemplateArgumentKind'
    

class ExceptionSpecificationKind(BaseEnumeration):
    NONE: 'ExceptionSpecificationKind'
    DYNAMIC_NONE: 'ExceptionSpecificationKind'
    DYNAMIC: 'ExceptionSpecificationKind'
    MS_ANY: 'ExceptionSpecificationKind'
    BASIC_NOEXCEPT: 'ExceptionSpecificationKind'
    COMPUTED_NOEXCEPT: 'ExceptionSpecificationKind'
    UNEVALUATED: 'ExceptionSpecificationKind'
    UNINSTANTIATED: 'ExceptionSpecificationKind'
    UNPARSED: 'ExceptionSpecificationKind'
    

class Cursor(Structure):
    @staticmethod
    def from_location(tu: 'TranslationUnit', location: 'SourceLocation') -> 'Cursor': ...

    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

    def is_abstract_record(self) -> bool: ...
    def is_anonymous(self) -> bool: ...
    def is_bitfield(self) -> bool: ...
    def is_const_method(self) -> bool: ...
    def is_converting_constructor(self) -> bool: ...
    def is_copy_constructor(self) -> bool: ...
    def is_default_constructor(self) -> bool: ...
    def is_default_method(self) -> bool: ...
    def is_definition(self) -> bool: ...
    def is_move_constructor(self) -> bool: ...
    def is_mutable_field(self) -> bool: ...
    def is_pure_virtual_method(self) -> bool: ...
    def is_scoped_enum(self) -> bool: ...
    def is_static_method(self) -> bool: ...
    def is_virtual_method(self) -> bool: ...
    
    def get_definition(self) -> typing.Optional['Cursor']: ...
    def get_usr(self) -> str: ...
    def get_included_file(self) -> 'File': ...

    @property
    def kind(self) -> CursorKind: ...
    @property
    def spelling(self) -> str: ...
    @property
    def displayname(self) -> str: ...
    @property
    def mangled_name(self) -> str: ...
    @property
    def location(self) -> 'SourceLocation': ...
    @property
    def linkage(self) -> 'LinkageKind': ...
    @property
    def tls_kind(self) -> 'TLSKind': ...
    @property
    def extent(self) -> 'SourceRange': ...
    @property
    def storage_class(self) -> 'StorageClass': ...
    @property
    def availability(self) -> 'AvailabilityKind': ...
    @property
    def access_specifier(self) -> 'AccessSpecifier': ...
    @property
    def type(self) -> 'Type': ...
    @property
    def canonical(self) -> 'Cursor': ...
    @property
    def result_type(self) -> 'Type': ...
    @property
    def exception_specification_kind(self) -> 'ExceptionSpecificationKind': ...
    @property
    def underlying_typedef_type(self) -> 'Type': ...
    @property
    def enum_type(self) -> 'Type': ...
    @property
    def enum_value(self) -> int: ...
    @property
    def objc_type_encoding(self) -> str: ...
    @property
    def hash(self) -> int: ...
    @property
    def semantic_parent(self) -> 'Cursor': ...
    @property
    def lexical_parent(self) -> 'Cursor': ...
    @property
    def translation_unit(self) -> 'TranslationUnit': ...
    @property
    def referenced(self) -> 'Cursor': ...
    @property
    def brief_comment(self) -> typing.Optional[str]: ...
    @property
    def raw_comment(self) -> typing.Optional[str]: ...

    def get_arguments(self) -> typing.Iterable['Cursor']: ...
    def get_num_template_arguments(self) -> int: ...
    def get_template_argument_kind(self, num: int) -> 'TemplateArgumentKind': ...
    def get_template_argument_type(self, num: int) -> 'Type': ...
    def get_template_argument_value(self, num: int) -> int: ...
    def get_template_argument_unsigned_value(self, num: int) -> int: ...
    def get_children(self) -> typing.Iterable['Cursor']: ...
    def walk_preorder(self) -> typing.Iterable['Cursor']: ...
    def get_tokens(self) -> typing.Iterable['Token']: ...
    def get_field_offsetof(self) -> int: ...
    def get_bitfield_width(self) -> int: ...

    @staticmethod
    def from_result(res: 'Cursor', fn: typing.Any, args: typing.Sequence[typing.Any]) -> 'Cursor': ...


class StorageClass():
    def __init__(self, value: int) -> None: ...
    def from_param(self) -> int: ...
    @property
    def name(self) -> str: ...
    @staticmethod
    def from_id(id: int) -> 'StorageClass': ...

    INVALID: 'StorageClass'
    NONE: 'StorageClass'
    EXTERN: 'StorageClass'
    STATIC: 'StorageClass'
    PRIVATEEXTERN: 'StorageClass'
    OPENCLWORKGROUPLOCAL: 'StorageClass'
    AUTO: 'StorageClass'
    REGISTER: 'StorageClass'
    

class AvailabilityKind(BaseEnumeration):
    AVAILABLE: 'AvailabilityKind'
    DEPRECATED: 'AvailabilityKind'
    NOT_AVAILABLE: 'AvailabilityKind'
    NOT_ACCESSIBLE: 'AvailabilityKind'
    

class AccessSpecifier(BaseEnumeration):
    INVALID: 'AccessSpecifier'
    PUBLIC: 'AccessSpecifier'
    PROTECTED: 'AccessSpecifier'
    PRIVATE: 'AccessSpecifier'
    NONE: 'AccessSpecifier'
    

class TypeKind(BaseEnumeration):
    @property
    def spelling(self) -> str: ...

    INVALID: 'TypeKind'
    UNEXPOSED: 'TypeKind'
    VOID: 'TypeKind'
    BOOL: 'TypeKind'
    CHAR_U: 'TypeKind'
    UCHAR: 'TypeKind'
    CHAR16: 'TypeKind'
    CHAR32: 'TypeKind'
    USHORT: 'TypeKind'
    UINT: 'TypeKind'
    ULONG: 'TypeKind'
    ULONGLONG: 'TypeKind'
    UINT128: 'TypeKind'
    CHAR_S: 'TypeKind'
    SCHAR: 'TypeKind'
    WCHAR: 'TypeKind'
    SHORT: 'TypeKind'
    INT: 'TypeKind'
    LONG: 'TypeKind'
    LONGLONG: 'TypeKind'
    INT128: 'TypeKind'
    FLOAT: 'TypeKind'
    DOUBLE: 'TypeKind'
    LONGDOUBLE: 'TypeKind'
    NULLPTR: 'TypeKind'
    OVERLOAD: 'TypeKind'
    DEPENDENT: 'TypeKind'
    OBJCID: 'TypeKind'
    OBJCCLASS: 'TypeKind'
    OBJCSEL: 'TypeKind'
    FLOAT128: 'TypeKind'
    HALF: 'TypeKind'
    IBM128: 'TypeKind'
    COMPLEX: 'TypeKind'
    POINTER: 'TypeKind'
    BLOCKPOINTER: 'TypeKind'
    LVALUEREFERENCE: 'TypeKind'
    RVALUEREFERENCE: 'TypeKind'
    RECORD: 'TypeKind'
    ENUM: 'TypeKind'
    TYPEDEF: 'TypeKind'
    OBJCINTERFACE: 'TypeKind'
    OBJCOBJECTPOINTER: 'TypeKind'
    FUNCTIONNOPROTO: 'TypeKind'
    FUNCTIONPROTO: 'TypeKind'
    CONSTANTARRAY: 'TypeKind'
    VECTOR: 'TypeKind'
    INCOMPLETEARRAY: 'TypeKind'
    VARIABLEARRAY: 'TypeKind'
    DEPENDENTSIZEDARRAY: 'TypeKind'
    MEMBERPOINTER: 'TypeKind'
    AUTO: 'TypeKind'
    ELABORATED: 'TypeKind'
    PIPE: 'TypeKind'
    OCLIMAGE1DRO: 'TypeKind'
    OCLIMAGE1DARRAYRO: 'TypeKind'
    OCLIMAGE1DBUFFERRO: 'TypeKind'
    OCLIMAGE2DRO: 'TypeKind'
    OCLIMAGE2DARRAYRO: 'TypeKind'
    OCLIMAGE2DDEPTHRO: 'TypeKind'
    OCLIMAGE2DARRAYDEPTHRO: 'TypeKind'
    OCLIMAGE2DMSAARO: 'TypeKind'
    OCLIMAGE2DARRAYMSAARO: 'TypeKind'
    OCLIMAGE2DMSAADEPTHRO: 'TypeKind'
    OCLIMAGE2DARRAYMSAADEPTHRO: 'TypeKind'
    OCLIMAGE3DRO: 'TypeKind'
    OCLIMAGE1DWO: 'TypeKind'
    OCLIMAGE1DARRAYWO: 'TypeKind'
    OCLIMAGE1DBUFFERWO: 'TypeKind'
    OCLIMAGE2DWO: 'TypeKind'
    OCLIMAGE2DARRAYWO: 'TypeKind'
    OCLIMAGE2DDEPTHWO: 'TypeKind'
    OCLIMAGE2DARRAYDEPTHWO: 'TypeKind'
    OCLIMAGE2DMSAAWO: 'TypeKind'
    OCLIMAGE2DARRAYMSAAWO: 'TypeKind'
    OCLIMAGE2DMSAADEPTHWO: 'TypeKind'
    OCLIMAGE2DARRAYMSAADEPTHWO: 'TypeKind'
    OCLIMAGE3DWO: 'TypeKind'
    OCLIMAGE1DRW: 'TypeKind'
    OCLIMAGE1DARRAYRW: 'TypeKind'
    OCLIMAGE1DBUFFERRW: 'TypeKind'
    OCLIMAGE2DRW: 'TypeKind'
    OCLIMAGE2DARRAYRW: 'TypeKind'
    OCLIMAGE2DDEPTHRW: 'TypeKind'
    OCLIMAGE2DARRAYDEPTHRW: 'TypeKind'
    OCLIMAGE2DMSAARW: 'TypeKind'
    OCLIMAGE2DARRAYMSAARW: 'TypeKind'
    OCLIMAGE2DMSAADEPTHRW: 'TypeKind'
    OCLIMAGE2DARRAYMSAADEPTHRW: 'TypeKind'
    OCLIMAGE3DRW: 'TypeKind'
    OCLSAMPLER: 'TypeKind'
    OCLEVENT: 'TypeKind'
    OCLQUEUE: 'TypeKind'
    OCLRESERVEID: 'TypeKind'
    EXTVECTOR: 'TypeKind'
    ATOMIC: 'TypeKind'
    

class RefQualifierKind(BaseEnumeration):
    NONE: 'RefQualifierKind'
    LVALUE: 'RefQualifierKind'
    RVALUE: 'RefQualifierKind'
    

class LinkageKind(BaseEnumeration):
    INVALID: 'LinkageKind'
    NO_LINKAGE: 'LinkageKind'
    INTERNAL: 'LinkageKind'
    UNIQUE_EXTERNAL: 'LinkageKind'
    EXTERNAL: 'LinkageKind'
    

class TLSKind(BaseEnumeration):
    NONE: 'TLSKind'
    DYNAMIC: 'TLSKind'
    STATIC: 'TLSKind'
    

class Type(Structure):
    @property
    def kind(self) -> 'TypeKind': ...
    def argument_types(self) -> typing.Iterator['Type']: ...
    @property
    def element_type(self) -> 'Type': ...
    @property
    def element_count(self) -> int: ...
    @property
    def translation_unit(self) -> 'TranslationUnit': ...
    def get_num_template_arguments(self) -> int: ...
    def get_template_argument_type(self, num: int) -> 'Type': ...
    def get_canonical(self) -> 'Type': ...
    def is_const_qualified(self) -> bool: ...
    def is_volatile_qualified(self) -> bool: ...
    def is_restrict_qualified(self) -> bool: ...
    def is_function_variadic(self) -> bool: ...
    def get_address_space(self) -> int: ...
    def get_typedef_name(self) -> str: ...
    def is_pod(self) -> bool: ...
    def get_pointee(self) -> 'Type': ...
    def get_declaration(self) -> 'Cursor': ...
    def get_result(self) -> 'Type': ...
    def get_array_element_type(self) -> 'Type': ...
    def get_array_size(self) -> int: ...
    def get_class_type(self) -> 'Type': ...
    def get_named_type(self) -> 'Type': ...
    def get_align(self) -> int: ...
    def get_size(self) -> int: ...
    def get_offset(self, fieldname) -> int: ...
    def get_ref_qualifier(self) -> 'RefQualifierKind': ...
    def get_fields(self) -> typing.Iterable['Cursor']: ...
    def get_exception_specification_kind(self) -> 'ExceptionSpecificationKind': ...
    @property
    def spelling(self) -> str: ...

    def __eq__(self, other: typing.Any) -> bool: ...
    def __ne__(self, other: typing.Any) -> bool: ...


class ClangObject():
    def __init__(self, obj: typing.Any) -> None: ...
    def from_param(self) -> _CObjectPtr: ...


SpellingCache: typing.Dict[int, 'CompletionChunk']

class CompletionChunk():
    class Kind():
        def __init__(self, name: str) -> None: ...
        def __str__(self) -> str: ...
        def __repr__(self) -> str: ...

    def __init__(self, completionString: str, key: int) -> None: ...
    def __repr__(self) -> str: ...

    @property
    def spelling(self) -> str: ...
    @property
    def kind(self) -> 'Kind': ...
    @property
    def string(self) -> str: ...

    def isKindOptional(self) -> bool: ...
    def isKindTypedText(self) -> bool: ...
    def isKindPlaceHolder(self) -> bool: ...
    def isKindInformative(self) -> bool: ...
    def isKindResultType(self) -> bool: ...

completionChunkKindMap: typing.Dict[int, CompletionChunk.Kind]


class CompletionString(ClangObject):
    class Availability():
        def __init__(self, name: str) -> None: ...
        def __str__(self) -> str: ...
        def __repr__(self) -> str: ...
        name: str

    def __len__(self) -> int: ...
    @property
    def num_chunks(self) -> int: ...
    def __getitem__(self, key: int) -> 'CompletionChunk': ...
    @property
    def priority(self) -> int: ...
    @property
    def availability(self) -> CompletionChunk.Kind: ...  # FIXME: This seems incorrect
    @property
    def briefComment(self) -> str: ...
    def __repr__(self) -> str: ...

availabilityKinds: typing.Dict[int, CompletionChunk.Kind]


class CodeCompletionResult(Structure):
    def __repr__(self) -> str: ...
    @property
    def kind(self) -> 'CursorKind': ...
    @property
    def string(self) -> CompletionString: ...


class CCRStructure(Structure):
    def __len__(self) -> int: ...
    def __getitem__(self, key: int) -> CodeCompletionResult: ...


class CodeCompletionResults(ClangObject):
    def __del__(self) -> None: ...
    @property
    def results(self) -> CCRStructure: ...
    @property
    def diagnostics(self) -> typing.Sequence['Diagnostic']: ...


class Index(ClangObject):
    @staticmethod
    def create(excludeDecls: bool = ...) -> 'Index': ...
    def __del__(self) -> None: ...
    def read(self, path: str) -> 'TranslationUnit': ...
    def parse(self,
              path: str,
              args: typing.Optional[typing.List[str]] = ...,
              unsaved_files: typing.Optional[typing.List[typing.Tuple[str, str]]] = ...,
              options: int = ...
              ) -> 'TranslationUnit': ...


class TranslationUnit(ClangObject):
    PARSE_NONE: int
    PARSE_DETAILED_PROCESSING_RECORD: int
    PARSE_INCOMPLETE: int
    PARSE_PRECOMPILED_PREAMBLE: int
    PARSE_CACHE_COMPLETION_RESULTS: int
    PARSE_SKIP_FUNCTION_BODIES: int
    PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION: int

    @classmethod
    def from_source(cls,
                    filename: str,
                    args: typing.Optional[typing.List[str]] = ...,
                    unsaved_files: typing.Optional[typing.List[typing.Tuple[str, str]]] = ...,
                    options: int = ...,
                    index: typing.Optional['Index'] = ...
                    ) -> 'TranslationUnit': ...

    @classmethod
    def from_ast_file(cls, filename: str, index: typing.Optional['Index'] = ...) -> 'TranslationUnit': ...

    def __del__(self) -> None: ...
    @property
    def cursor(self) -> 'Cursor': ...
    @property
    def spelling(self) -> str: ...
    def get_includes(self) -> typing.Iterable['FileInclusion']: ...
    def get_file(self, filename: str) -> 'File': ...
    def get_location(self,
                     filename: str,
                     position: typing.Union[int, typing.Tuple[int, int]]
                     ) -> 'SourceLocation': ...
    def get_extent(self,
                   filename: str,
                   locations: typing.Union[typing.Tuple['SourceLocation', 'SourceLocation'],
                                           typing.Tuple[int, int],
                                           typing.Tuple[typing.Tuple[int, int], typing.Tuple[int, int]]]
                   ) -> 'SourceRange': ...
    @property
    def diagnostics(self) -> typing.Sequence['Diagnostic']: ...
    def reparse(self,
                unsaved_files: typing.Optional[typing.List[typing.Tuple[str, str]]] = ...,
                options: int = ...
                ) -> None: ...
    def save(self, filename: str) -> None: ...
    def codeComplete(self,
                     path: str,
                     line: int,
                     column: int,
                     unsaved_files: typing.Optional[typing.List[typing.Tuple[str, str]]] = ...,
                     include_macros: bool = ...,
                     include_code_patterns: bool = ...,
                     include_brief_comments: bool = ...
                     ) -> typing.Optional['CodeCompletionResults']: ...
    def get_tokens(self,
                   locations: typing.Optional[typing.Tuple['SourceLocation', 'SourceLocation']] = ...,
                   extent: typing.Optional['SourceRange'] = ...
                   ) -> typing.Iterable['Token']: ...


class File(ClangObject):
    @staticmethod
    def from_name(translation_unit: 'TranslationUnit', file_name: str) -> 'File': ...
    @property
    def name(self) -> str: ...
    @property
    def time(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...


class FileInclusion():
    def __init__(self, src: str, tgt: 'File', loc: 'SourceLocation', depth: int) -> None: ...

    source: str
    include: 'File'
    location: 'SourceLocation'
    depth: int
    @property
    def is_input_file(self) -> bool: ...


class CompilationDatabaseError(Exception):
    ERROR_UNKNOWN: int
    ERROR_CANNOTLOADDATABASE: int

    def __init__(self, enumeration: int, message: str) -> None: ...


class CompileCommand():
    @property
    def directory(self) -> str: ...
    @property
    def filename(self) -> str: ...
    @property
    def arguments(self) -> typing.Iterable[str]: ...


class CompileCommands():
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i: int) -> 'CompileCommand': ...


class CompilationDatabase(ClangObject):
    def __del__(self) -> None: ...
    @staticmethod
    def fromDirectory(buildDir: str) -> 'CompilationDatabase': ...
    def getCompileCommands(self, filename: str) -> 'CompileCommands': ...
    def getAllCompileCommands(self) -> 'CompileCommands': ...


class Token(Structure):
    @property
    def spelling(self) -> str: ...
    @property
    def kind(self) -> 'TokenKind': ...
    @property
    def location(self) -> 'SourceLocation': ...
    @property
    def extent(self) -> 'SourceRange': ...
    @property
    def cursor(self) -> 'Cursor': ...


class Config():
    library_path: typing.Optional[str]
    library_file: typing.Optional[str]
    compatibility_check: bool
    loaded: bool

    @staticmethod
    def set_library_path(path: str) -> None: ...
    @staticmethod
    def set_library_file(filename: str) -> None: ...
    @staticmethod
    def set_compatibility_check(check_status: bool) -> None: ...
    @property
    def lib(self) -> CDLL: ...
    def get_filename(self) -> str: ...
    def get_cindex_library(self) -> CDLL: ...
    def function_exists(self, name: str) -> bool: ...
